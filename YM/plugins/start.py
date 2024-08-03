from pyrogram import Client, filters

@Client.on_message(filters.command(["start", "help"]))
async def start_comm(c, m):
    await m.reply_text("I am Working Broo")
