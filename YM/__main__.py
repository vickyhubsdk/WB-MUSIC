from fastapi import FastAPI
from socketio import ASGIApp, Server
import asyncio
from bot import bot
from config import LOG_GROUP_ID
app = FastAPI()

sio = Server(async_mode="asgi")
app_asgi = ASGIApp(sio, app)

from fastapi.staticfiles import StaticFiles
app.mount("/static", StaticFiles(directory="YM/static"), name="static")

@app.get("/")
async def read_index():
    return fastapi.responses.HTMLResponse(open("YM/templates/index.html").read())

async def run_bot():
    await bot.start()
    try:
        bot.send_message(LOG_GROUP_ID, "Started")
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

import threading
threading.Thread(target=start_bot).start()
