from fastapi import FastAPI, Request
from aiogram import Bot, Dispatcher
from aiogram.types import Update

from bot.config import BOT_TOKEN
from bot.handlers import menu, user

app = FastAPI()

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

dp.include_router(menu.router)
dp.include_router(user.router)


@app.post("/webhook")
async def telegram_webhook(request: Request):
    data = await request.json()
    update = Update.model_validate(data)
    await dp.feed_update(bot, update)
    return {"status": "ok"}
