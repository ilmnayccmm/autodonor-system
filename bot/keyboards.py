from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def main_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton(text="🔧 Послуги"))
    kb.add(KeyboardButton(text="📝 Запис / Заявка"))
    kb.add(KeyboardButton(text="🕒 Графік роботи"))
    kb.add(KeyboardButton(text="📍 Контакти"))
    kb.add(KeyboardButton(text="🚚 Евакуатор"))
    return kb


def services_keyboard():
    services = [
        "Комп’ютерна діагностика",
        "Ремонт турбін",
        "Реставрація рульових рейок",
        "Реставрація форсунок 1.5 DCI",
        "Ремонт двигунів",
        "Ремонт ходової",
        "Вулканізація",
        "Кондиціонування",
        "Імпортні автозапчастини",
        "Евакуатор"
    ]

    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    for s in services:
        kb.add(KeyboardButton(text=s))

    kb.add(KeyboardButton(text="⬅ Назад"))
    return kb
