from fastapi import FastAPI
from aiogram import Bot, Dispatcher

app = FastAPI()
bot = Bot("TOKEN")
dp = Dispatcher()

@app.post("/webhook")
async def webhook(update: dict):
    await dp.feed_webhook_update(bot, update)
