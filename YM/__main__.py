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

load_dotenv()

app_asgi = FastAPI()

@app_asgi.get("/")
async def root():
    return {"message": "Hello, World!"}

sio = socketio.AsyncServer(async_mode='asgi')
app = FastAPI()
sio_app = socketio.ASGIApp(sio, other_asgi_app=app)

app.mount("/static", StaticFiles(directory="YM/static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("YM/templates/index.html", "r") as f:
        return HTMLResponse(content=f.read(), status_code=200)

@sio.event
async def message(sid, data):
    print("SocketIO message:", data)
    await sio.emit('response', f"Message received: {data}")

async def start_bot():
    await bot.start()
    await idle()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(start_bot())
    uvicorn.run(sio_app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
