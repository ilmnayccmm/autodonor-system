import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_PASS = os.getenv("DB_PASS")

    JWT_SECRET = os.getenv("JWT_SECRET")
    JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")
    JWT_EXPIRE_MINUTES = int(os.getenv("JWT_EXPIRE_MINUTES"))

settings = Settings()

BOT_TOKEN = os.getenv("BOT_TOKEN", "8443842958:AAH3qi7xKfehSz0iwqg77R5cMvq28JIOegs")
ADMIN_TG = "@" + os.getenv("ADMIN_TG")


STO_NAME = "СТО Автодонор"

ADDRESS = "вул. Ремонтна, 8, Угринів, Івано-Франківська область, 77423"
PHONE = "098 199 1246"

SCHEDULE = """
Понеділок: 09:00–18:00
Вівторок: 09:00–18:00
Середа: 09:00–18:00
Четвер: 09:00–18:00
П’ятниця: 09:00–18:00
Субота: Зачинено
Неділя: Зачинено
"""

SERVICES = [
    "Комп’ютерна діагностика",
    "Ремонт турбін",
    "Реставрація рульових рейок",
    "Реставрація форсунок 1.5 DCI",
    "Ремонт двигунів",
    "Ремонт ходової частини",
    "Вулканізація",
    "Кондиціонування",
    "Імпортні автозапчастини",
    "Паливні форсунки для дизельних авто",
    "Послуги евакуатора"
]

if not BOT_TOKEN:
    raise ValueError("❌ BOT_TOKEN не знайдено в .env файлі")

