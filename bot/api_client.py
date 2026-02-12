import requests
from bot.config import API_URL, BOT_API_KEY

HEADERS = {
    "Authorization": f"Bearer {BOT_API_KEY}"
}


def get_services():
    r = requests.get(f"{API_URL}/services")
    return r.json()


def create_request(service_id: int, phone: str, comment: str):
    payload = {
        "service_id": service_id,
        "phone": phone,
        "comment": comment
    }
    r = requests.post(f"{API_URL}/requests", json=payload, headers=HEADERS)
    return r.json()
