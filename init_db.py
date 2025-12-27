import sqlite3
import os

DB_PATH = os.path.join("database", "database.db")

conn = sqlite3.connect(DB_PATH)

conn.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    category TEXT,
    description TEXT,
    amount REAL
)
""")

conn.close()

print("Database initialized successfully!")
