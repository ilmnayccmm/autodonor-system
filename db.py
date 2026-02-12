import sqlite3
from datetime import datetime

DB_NAME = "autodonor.db"


def init_db():
    conn = sqlite3.connect("autodonor.db")
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS requests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            service TEXT NOT NULL,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            comment TEXT,
            created_at TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def add_request(service: str, name: str, phone: str, comment: str):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO requests (service, name, phone, comment, created_at)
        VALUES (?, ?, ?, ?, ?)
    """, (service, name, phone, comment, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    conn.commit()
    conn.close()
