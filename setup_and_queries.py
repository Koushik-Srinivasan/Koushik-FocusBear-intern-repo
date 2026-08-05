"""
Introduction to SQL for Data Analysis - issue #18
Uses SQLite (via Python's built-in sqlite3) to practice SELECT, WHERE,
ORDER BY, GROUP BY, and HAVING against a small sample dataset.
"""

import sqlite3

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

# --- Setup: create and populate sample tables ---
cursor.execute("""
CREATE TABLE users (
    user_id INTEGER PRIMARY KEY,
    name TEXT,
    plan TEXT
)
""")

cursor.execute("""
CREATE TABLE sessions (
    session_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    focus_minutes INTEGER,
    device TEXT
)
""")

users = [
    (1, "Koushik", "premium"),
    (2, "Priya", "free"),
    (3, "Sam", "premium"),
    (4, "Alex", "free"),
]
sessions = [
    (1, 1, 45, "desktop"),
    (2, 1, 60, "mobile"),
    (3, 2, 30, "desktop"),
    (4, 3, 90, "desktop"),
    (5, 3, 75, "mobile"),
    (6, 4, 20, "mobile"),
]

cursor.executemany("INSERT INTO users VALUES (?, ?, ?)", users)
cursor.executemany("INSERT INTO sessions VALUES (?, ?, ?, ?)", sessions)
conn.commit()

def run(label, query):
    print(f"\n=== {label} ===")
    print(f"SQL: {query.strip()}")
    for row in cursor.execute(query):
        print(row)

# --- Simple SELECT ---
run("All users", "SELECT * FROM users")

# --- WHERE and ORDER BY ---
run(
    "Sessions over 40 minutes, sorted longest first",
    "SELECT * FROM sessions WHERE focus_minutes > 40 ORDER BY focus_minutes DESC"
)

# --- GROUP BY ---
run(
    "Total focus minutes per user",
    """
    SELECT user_id, SUM(focus_minutes) AS total_minutes
    FROM sessions
    GROUP BY user_id
    """
)

# --- GROUP BY with HAVING ---
run(
    "Users whose total focus minutes exceed 60",
    """
    SELECT user_id, SUM(focus_minutes) AS total_minutes
    FROM sessions
    GROUP BY user_id
    HAVING SUM(focus_minutes) > 60
    """
)

# --- JOIN, to connect it back to something meaningful (user names + plan) ---
run(
    "Total focus minutes per user, with name and plan",
    """
    SELECT users.name, users.plan, SUM(sessions.focus_minutes) AS total_minutes
    FROM sessions
    JOIN users ON sessions.user_id = users.user_id
    GROUP BY users.user_id
    HAVING SUM(sessions.focus_minutes) > 60
    ORDER BY total_minutes DESC
    """
)

conn.close()
