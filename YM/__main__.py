from fastapi import FastAPI
from socketio import ASGIApp, Server
import asyncio
from bot import bot
from config import LOG_GROUP_ID
from pyrogram import idle
import threading

app = FastAPI()

#sio = Server(async_mode="asgi")
sio = Server(async_mode="aiohttp")
app_asgi = ASGIApp(sio, app)

from fastapi.staticfiles import StaticFiles
app.mount("/static", StaticFiles(directory="YM/static"), name="static")

@app.get("/")
async def read_index():
    with open("YM/templates/index.html") as f:
        return fastapi.responses.HTMLResponse(f.read())

async def run_bot():
    await bot.start()
    try:
        await bot.send_message(LOG_GROUP_ID, "Started")
    except Exception:
        pass
    await idle()

def start_bot():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(run_bot())

@app.on_event("startup")
async def startup_event():
    loop = asyncio.get_event_loop()
    loop.create_task(run_bot())

# Start bot in a separate thread to avoid blocking the main thread
threading.Thread(target=start_bot).start()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app_asgi, host="0.0.0.0", port=8000)
