from sqlalchemy import create_engine, text
import os
import time

DATABASE_URL = os.getenv("DATABASE_URL")

engine = None

def init_db():
    global engine

    for i in range(10):
        try:
            engine = create_engine(DATABASE_URL)
            with engine.connect() as conn:
                conn.execute(text("SELECT 1"))
            print("✅ Connected to DB")
            return
        except Exception:
            print(f"⏳ DB chưa ready, retry {i+1}")
            time.sleep(2)

    raise Exception("❌ Cannot connect to DB")


def get_engine():
    return engine