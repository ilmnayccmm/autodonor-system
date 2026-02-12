import asyncio
from aiogram import Bot, Dispatcher
from bot.config import BOT_TOKEN
from bot.handlers import admin, menu, user

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

dp.include_router(admin.router)
dp.include_router(menu.router)
dp.include_router(user.router)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
