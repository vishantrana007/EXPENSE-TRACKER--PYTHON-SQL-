"""
db.py
Handles SQLite database connection and table creation for Expense Tracker.
Ensures database is always created inside:
<project>/EXPENSE TRACKER (PYTHON + SQL)/database/
"""

import sqlite3
import os

# -----------------------------
# Project Root (EXPENSE TRACKER (PYTHON + SQL))
# -----------------------------
# Current file = src/db.py → move one level up = EXPENSE TRACKER (PYTHON + SQL)
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Database folder path
DATABASE_FOLDER = os.path.join(PROJECT_ROOT, "database")
os.makedirs(DATABASE_FOLDER, exist_ok=True)  # create if missing

# Full path to DB file
DB_PATH = os.path.join(DATABASE_FOLDER, "expense_tracker.db")

# -----------------------------
# Database Connection
# -----------------------------
def get_connection():
    """
    Establish a connection to the SQLite database inside 'database' folder.
    """
    return sqlite3.connect(DB_PATH)

# -----------------------------
# Table Initialization
# -----------------------------
def create_table():
    """
    Creates the 'expenses' table if it does not already exist.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            category TEXT NOT NULL,
            description TEXT,
            amount REAL NOT NULL
        )
    """)
    conn.commit()
    conn.close()
