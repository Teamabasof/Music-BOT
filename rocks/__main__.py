from pyrogram import idle
from pyrogram import Client as Bot
from rocks.clientbot import run
from rocks.config import API_ID, API_HASH, BOT_TOKEN


bot = Bot(
    ":memory:", API_ID, API_HASH, bot_token=BOT_TOKEN, plugins=dict(root="harshit")
)

bot.start()
run()
idle()
