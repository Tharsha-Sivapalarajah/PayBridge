import sqlite3
from datetime import datetime

DB_NAME = "paybridge.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS processed_payments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            payment_id TEXT UNIQUE,
            processed_at TEXT
        )
    """)

    conn.commit()
    conn.close()


def is_payment_processed(payment_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT 1 FROM processed_payments WHERE payment_id = ?",
        (payment_id,)
    )

    result = cursor.fetchone()
    conn.close()

    return result is not None


def mark_payment_processed(payment_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO processed_payments (payment_id, processed_at) VALUES (?, ?)",
        (payment_id, datetime.utcnow().isoformat())
    )

    conn.commit()
    conn.close()
