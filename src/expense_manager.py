"""
expense_manager.py
Handles all database operations for Expense Tracker.
Ensures database is always created inside:
<project>/EXPENSE TRACKER (PYTHON + SQL)/database/
"""

import sqlite3
import os
from datetime import datetime

# -----------------------------
# Project Root (EXPENSE TRACKER (PYTHON + SQL))
# -----------------------------
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Database folder path
DATABASE_FOLDER = os.path.join(PROJECT_ROOT, "database")
os.makedirs(DATABASE_FOLDER, exist_ok=True)

# Full path to DB file
DB_PATH = os.path.join(DATABASE_FOLDER, "expense_tracker.db")

# -----------------------------
# Add Expense
# -----------------------------
def add_expense(date, category, description, amount):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO expenses (date, category, description, amount)
        VALUES (?, ?, ?, ?)
    """, (date, category, description, amount))
    conn.commit()
    conn.close()

# -----------------------------
# View All Expenses
# -----------------------------
def get_all_expenses():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses ORDER BY date DESC")
    rows = cursor.fetchall()
    conn.close()
    return rows

# -----------------------------
# Update Expense
# -----------------------------
def update_expense(exp_id, date, category, description, amount):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE expenses
        SET date = ?, category = ?, description = ?, amount = ?
        WHERE id = ?
    """, (date, category, description, amount, exp_id))
    conn.commit()
    conn.close()

# -----------------------------
# Delete Expense
# -----------------------------
def delete_expense(exp_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM expenses WHERE id = ?", (exp_id,))
    conn.commit()
    conn.close()

# -----------------------------
# Monthly Summary
# -----------------------------
def get_monthly_summary():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT strftime('%Y-%m', date) as month, SUM(amount)
        FROM expenses
        GROUP BY month
        ORDER BY month DESC
    """)
    rows = cursor.fetchall()
    conn.close()
    return rows

# -----------------------------
# Category-wise Report
# -----------------------------
def get_category_report():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT category, SUM(amount)
        FROM expenses
        GROUP BY category
    """)
    rows = cursor.fetchall()
    conn.close()
    return rows

# -----------------------------
# Spending Insights
# -----------------------------
def view_spending_insights():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    insights = []

    cursor.execute("SELECT SUM(amount) FROM expenses")
    total = cursor.fetchone()[0] or 0
    insights.append(f"Total expenses recorded: {total}")

    cursor.execute("""
        SELECT category, SUM(amount) as total
        FROM expenses
        GROUP BY category
        ORDER BY total DESC
        LIMIT 1
    """)
    row = cursor.fetchone()
    if row:
        insights.append(f"Highest spending category: {row[0]} ({row[1]})")
    else:
        insights.append("No category spending data available.")

    cursor.execute("""
        SELECT date, category, description, amount
        FROM expenses
        ORDER BY date DESC
        LIMIT 1
    """)
    row = cursor.fetchone()
    if row:
        insights.append(f"Most recent expense: {row[0]} | {row[1]} | {row[2]} | {row[3]}")
    else:
        insights.append("No recent expense available.")

    conn.close()
    return insights
