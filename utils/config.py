import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    BASE_URL = os.getenv("BASE_URL", "https://example.com")
    API_BASE_URL = os.getenv("API_BASE_URL", "https://jsonplaceholder.typicode.com")

    DB_NAME = os.getenv("DB_NAME", "testdb")
    DB_USER = os.getenv("DB_USER", "postgres")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "password")
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = os.getenv("DB_PORT", "5432")
