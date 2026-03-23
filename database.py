import sqlite3
from datetime import datetime

# Connect to database
def connect_db():
    conn = sqlite3.connect("study.db")
    return conn

# Create table
def create_table():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS quizzes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT,
        created_at TEXT
    )
    """)

    conn.commit()
    conn.close()

# Save quiz
def save_quiz(questions):
    conn = connect_db()
    cursor = conn.cursor()

    for q in questions:
        cursor.execute(
            "INSERT INTO quizzes (question, created_at) VALUES (?, ?)",
            (q, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        )

    conn.commit()
    conn.close()

# Get all quizzes
def get_quizzes():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM quizzes ORDER BY id DESC")
    data = cursor.fetchall()

    conn.close()
    return data