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
import threading

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
    print("SocketIO message:", data)
    await sio.emit('response', f"Message received: {data}")

async def start_bot():
    await bot.start()
    bot.send_message(-1002146211959, "Started")
    await idle()

def run_uvicorn():
    uvicorn.run(sio_app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)), workers=1)

if __name__ == "__main__":
    # Run bot in a separate thread
    bot_thread = threading.Thread(target=lambda: asyncio.run(start_bot()))
    bot_thread.start()
    
    # Run FastAPI with Uvicorn
    run_uvicorn()
