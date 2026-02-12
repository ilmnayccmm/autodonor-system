from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from bot.keyboards import main_menu, services_keyboard
from bot.api_client import get_services
from bot.states import RequestForm
from aiogram.fsm.context import FSMContext

router = Router()


@router.message(Command("start", "menu"))
async def start(message: Message):
    await message.answer(
        "🚗 СТО Автодонор\nОберіть дію:",
        reply_markup=main_menu()
    )


@router.callback_query(lambda c: c.data == "menu_services")
async def menu_services(call: CallbackQuery):
    services = get_services()
    await call.message.answer("🔧 Наші послуги:", reply_markup=services_keyboard(services))


@router.callback_query(lambda c: c.data == "menu_request")
async def menu_request(call: CallbackQuery, state: FSMContext):
    services = get_services()
    await call.message.answer("Оберіть послугу:", reply_markup=services_keyboard(services))
    await state.set_state(RequestForm.service)
