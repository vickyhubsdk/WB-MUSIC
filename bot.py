import asyncio
from pyrogram import Client, idle
from config import API_ID, API_HASH, BOT_TOKEN, LOG_GROUP_ID

bot = Client(
      "my_bot", 
      api_id=API_ID, 
      api_hash=API_HASH, 
      bot_token=BOT_TOKEN,
      plugins = dict(root="YM.plugins")
    )
async def run_bot():
    await bot.start()
    try:
        await bot.send_message(LOG_GROUP_ID, "Bot Started")
    except Exception:
      pass
    await idle()
