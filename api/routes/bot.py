from fastapi import APIRouter, Request
import json
import httpx
import os

router = APIRouter()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_API = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}"

@router.post("/bot/webhook")
async def telegram_webhook(request: Request):
    data = await request.json()
    print("TELEGRAM UPDATE:", data)


    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")


        if text == "/start":
            reply = "🚗 Вітаю! Це бот Автодонор.\n\nДоступні команди:\n/services\n/help"
        elif text == "/help":
            reply = "ℹ️ Допомога:\n/services — список послуг\n/request — залишити заявку"
        else:
            reply = f"Ти написав: {text}"

        async with httpx.AsyncClient() as client:
            await client.post(
                f"{TELEGRAM_API}/sendMessage",
                json={
                    "chat_id": chat_id,
                    "text": reply
                }
            )

    return {"ok": True}
