import os

class Config:
    ERP_BASE_URL = os.getenv("ERP_BASE_URL", "http://localhost:5000")
    MAX_RETRIES = int(os.getenv("MAX_RETRIES", 3))
    RETRY_DELAY = int(os.getenv("RETRY_DELAY", 2))
    DATABASE_NAME = os.getenv("DATABASE_NAME", "paybridge.db")
    ALLOWED_CURRENCIES = ["USD", "LKR", "EUR"]
