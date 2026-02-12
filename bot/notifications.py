from aiogram import Bot
from bot.config import ADMIN_ID, BOT_TOKEN

bot = Bot(token=BOT_TOKEN)


async def notify_admin(req: dict):
    text = (
        "📥 Нова заявка\n\n"
        f"ID: {req['id']}\n"
        f"Телефон: {req['phone']}\n"
        f"Статус: {req['status']}"
    )
    await bot.send_message(ADMIN_ID, text)
