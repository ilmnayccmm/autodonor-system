import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage

from config import *
from db import init_db, add_request

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

init_db()

# ---------- FSM ----------

class RequestState(StatesGroup):
    choosing_service = State()
    waiting_phone = State()

# ---------- КНОПКИ ----------

def main_menu():
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🔧 Послуги"), KeyboardButton(text="📝 Запис / Заявка")],
            [KeyboardButton(text="🕒 Графік роботи"), KeyboardButton(text="📍 Контакти")],
            [KeyboardButton(text="🚚 Евакуатор")]
        ],
        resize_keyboard=True
    )
    return kb

def services_menu():
    buttons = [[KeyboardButton(text=s)] for s in SERVICES]
    buttons.append([KeyboardButton(text="⬅ Назад")])
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

# ---------- КОМАНДИ ----------

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        f"Вітаємо у {STO_NAME} 👋\n\nОберіть дію з меню 👇",
        reply_markup=main_menu()
    )

@dp.message(Command("menu"))
async def menu(message: types.Message):
    await message.answer("📌 Головне меню:", reply_markup=main_menu())

# ---------- КНОПКИ ----------

@dp.message(lambda msg: msg.text == "🔧 Послуги")
async def show_services(message: types.Message, state: FSMContext):
    await state.set_state(RequestState.choosing_service)
    await message.answer("🔧 Оберіть послугу:", reply_markup=services_menu())

@dp.message(RequestState.choosing_service)
async def choose_service(message: types.Message, state: FSMContext):
    if message.text == "⬅ Назад":
        await state.clear()
        await message.answer("🔙 Головне меню", reply_markup=main_menu())
        return

    if message.text not in SERVICES:
        await message.answer("❌ Оберіть послугу з кнопок")
        return

    await state.update_data(service=message.text)
    await state.set_state(RequestState.waiting_phone)

    await message.answer(
        f"✅ Ви обрали послугу:\n<b>{message.text}</b>\n\n📞 Введіть номер телефону:",
        parse_mode="HTML"
    )

@dp.message(RequestState.waiting_phone)
async def save_request_handler(message: types.Message, state: FSMContext):
    phone = message.text.strip()

    if not phone.isdigit() or len(phone) < 9:
        await message.answer("❌ Введіть коректний номер телефону")
        return

    data = await state.get_data()
    service = data.get("service")

    add_request(
        user_id=message.from_user.id,
        username=message.from_user.username,
        service=service,
        phone=phone
    )

    await message.answer(
        "✅ Заявку прийнято!\n\nНаш адміністратор зв’яжеться з вами найближчим часом 📞",
        reply_markup=main_menu()
    )

    await state.clear()

# ---------- ІНФО ----------

@dp.message(lambda msg: msg.text == "🕒 Графік роботи")
async def schedule(message: types.Message):
    await message.answer(f"🕒 Графік роботи:\n{SCHEDULE}")

@dp.message(lambda msg: msg.text == "📍 Контакти")
async def contacts(message: types.Message):
    await message.answer(
        f"📍 Адреса: {ADDRESS}\n📞 Телефон: {PHONE}\n👨‍💼 Адміністратор: {ADMIN_TG}"
    )

@dp.message(lambda msg: msg.text == "🚚 Евакуатор")
async def evacuator(message: types.Message):
    await message.answer("🚚 Послуги евакуатора по Україні та за її межами.\n📞 Телефонуйте: 098 199 1246")

@dp.message(lambda msg: msg.text == "📝 Запис / Заявка")
async def request(message: types.Message, state: FSMContext):
    await state.set_state(RequestState.choosing_service)
    await message.answer("🔧 Оберіть послугу:", reply_markup=services_menu())

# ---------- ЗАПУСК ----------

async def main():
    print("✅ Бот запущено!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
