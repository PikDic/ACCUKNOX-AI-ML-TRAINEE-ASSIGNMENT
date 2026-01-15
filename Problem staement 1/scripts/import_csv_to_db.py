import csv
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "data" / "books.db"
CSV_PATH = BASE_DIR / "data" / "MOCK_DATA.csv"

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Create users table fresh
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        first_name TEXT,
        last_name TEXT,
        email TEXT,
        gender TEXT,
        ip_address TEXT
    )
""")

with open(CSV_PATH, newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        cursor.execute(
            """
            INSERT INTO users (
                user_id,
                first_name,
                last_name,
                email,
                gender,
                ip_address
            ) VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                row["id"],
                row["first_name"],
                row["last_name"],
                row["email"],
                row["gender"],
                row["ip_address"]
            )
        )

conn.commit()
conn.close()

print("User data imported from CSV successfully.")
