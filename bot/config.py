import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN", "8443842958:AAH3qi7xKfehSz0iwqg77R5cMvq28JIOegs")
API_URL = os.getenv("API_URL", "http://localhost:8000")
BOT_API_KEY = os.getenv("BOT_API_KEY", "8443842958:AAH3qi7xKfehSz0iwqg77R5cMvq28JIOegs")  # окремий ключ доступу бота
ADMIN_ID = int(os.getenv("ADMIN_TG_ID", "476459907"))
WEBHOOK_URL = os.getenv("WEBHOOK_URL")