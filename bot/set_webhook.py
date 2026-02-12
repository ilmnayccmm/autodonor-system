import asyncio
from aiogram import Bot
from bot.config import BOT_TOKEN, WEBHOOK_URL


async def main():
    bot = Bot(token=BOT_TOKEN)
    await bot.set_webhook(WEBHOOK_URL)
    print("✅ Webhook встановлено:", WEBHOOK_URL)

if __name__ == "__main__":
    asyncio.run(main())
