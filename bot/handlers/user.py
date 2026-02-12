from aiogram import Router
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext

from bot.states import RequestForm
from bot.api_client import create_request
from bot.notifications import notify_admin

router = Router()


@router.callback_query(lambda c: c.data.startswith("service_"))
async def select_service(call: CallbackQuery, state: FSMContext):
    service_id = int(call.data.split("_")[1])
    await state.update_data(service_id=service_id)
    await state.set_state(RequestForm.phone)
    await call.message.answer("📞 Введіть номер телефону:")


@router.message(RequestForm.phone)
async def input_phone(message: Message, state: FSMContext):
    await state.update_data(phone=message.text)
    await state.set_state(RequestForm.comment)
    await message.answer("💬 Коментар (або '-' якщо немає):")


@router.message(RequestForm.comment)
async def input_comment(message: Message, state: FSMContext):
    data = await state.get_data()

    req = create_request(
        service_id=data["service_id"],
        phone=data["phone"],
        comment=message.text
    )

    await notify_admin(req)

    await message.answer("✅ Заявка успішно створена! Ми з вами звʼяжемось.")
    await state.clear()
