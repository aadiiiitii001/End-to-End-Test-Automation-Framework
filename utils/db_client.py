import os
import psycopg2

class DBClient:

    @staticmethod
    def get_connection():
        return psycopg2.connect(
            dbname=os.getenv("DB_NAME", "testdb"),
            user=os.getenv("DB_USER", "postgres"),
            password=os.getenv("DB_PASSWORD", "password"),
            host=os.getenv("DB_HOST", "localhost"),
            port=os.getenv("DB_PORT", "5432"),
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
