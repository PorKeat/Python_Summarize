import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

def connect():
    try:
        connection = psycopg2.connect(
            database=os.getenv("POSTGRES_DB"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
            host=os.getenv("POSTGRES_HOST"),
            port=os.getenv("POSTGRES_PORT")
        )
        return connection
    except Exception as e:
        print(f"Error: {e}")
        return None
