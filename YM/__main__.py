from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import socketio
import asyncio
from bot import bot
from pyrogram import idle
import os
from dotenv import load_dotenv
import uvicorn
from YM import LOGGER
load_dotenv()

# Create FastAPI app instance
app = FastAPI()

# Configure static files directory
app.mount("/static", StaticFiles(directory="YM/static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("YM/templates/index.html", "r") as f:
        return HTMLResponse(content=f.read(), status_code=200)

# Configure Socket.IO server
sio = socketio.AsyncServer(async_mode='asgi')
sio_app = socketio.ASGIApp(sio, other_asgi_app=app)

@sio.event
async def message(sid, data):
    await sio.emit('response', f"Message received: {data}")

async def start_bot():
    LOGGER("YM").info("Starting bot...")
    await bot.start()
    await bot.send_message(-1002146211959, "Started")
    LOGGER("YM").info(f"Bot Started As {bot.me.first_name}")
    await idle()

async def start_server():
    config = uvicorn.Config(app=sio_app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)), workers=1)
    server = uvicorn.Server(config)
    LOGGER("YM").info("Starting Web Client")
    await server.serve()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(start_bot())
    loop.run_until_complete(start_server())
