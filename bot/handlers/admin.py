from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from bot.config import ADMIN_TG_ID
import requests
from bot.config import API_URL

router = Router()

def is_admin(user_id: int):
    return user_id == ADMIN_TG_ID

@router.message(Command("admin"))
async def admin_panel(msg: Message):
    if not is_admin(msg.from_user.id):
        await msg.answer("⛔ Доступ заборонено")
        return

    await msg.answer(
        "🧑‍💼 Адмін-панель:\n\n"
        "/requests - перегляд заявок\n"
        "/export - експорт заявок\n"
    )

@router.message(Command("requests"))
async def view_requests(msg: Message):
    if not is_admin(msg.from_user.id):
        return

    r = requests.get(f"{API_URL}/requests/all")
    data = r.json()

    if not data:
        await msg.answer("Заявок немає")
        return

    text = "📋 Заявки:\n\n"
    for req in data:
        text += f"#{req['id']} | {req['phone']} | {req['status']}\n"

    await msg.answer(text)

@router.message(Command("export"))
async def export_requests(msg: Message):
    if not is_admin(msg.from_user.id):
        return

    r = requests.get(f"{API_URL}/requests/export")
    await msg.answer("📦 Експорт виконано (CSV/JSON готовий)")
