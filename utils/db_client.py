import psycopg2
from utils.config import Config

class DBClient:

    @staticmethod
    def get_connection():
        return psycopg2.connect(
            dbname=Config.DB_NAME,
            user=Config.DB_USER,
            password=Config.DB_PASSWORD,
            host=Config.DB_HOST,
            port=Config.DB_PORT
        )

    @staticmethod
    def fetch_user(user_id):
        conn = DBClient.get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute("SELECT id FROM users WHERE id = %s", (user_id,))
            result = cursor.fetchone()
            return result
        finally:
            cursor.close()
            conn.close()
