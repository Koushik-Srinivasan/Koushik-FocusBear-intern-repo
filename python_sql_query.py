"""
Connect to PostgreSQL from Python with psycopg, load a query straight into a
Pandas DataFrame, and transform it. Part of issue #16, reuses the focusbear_dev
database and users/focus_sessions tables seeded in issue #15.
"""

import os

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# SQLAlchemy engine using the psycopg (v3) driver, this is what lets
# pandas.read_sql_query run without the "not a supported DBAPI2 connection" warning
engine = create_engine(
    f"postgresql+psycopg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

QUERY = """
    SELECT u.user_id, u.name, u.plan, s.session_date, s.focus_minutes, s.device
    FROM focus_sessions s
    JOIN users u ON u.user_id = s.user_id
    ORDER BY u.user_id, s.session_date;
"""

df = pd.read_sql_query(QUERY, engine)
print("Rows fetched:", len(df))
print(df)

# --- Transformations in Pandas ---

# Per-user rollup: total/average focus time and a simple engagement label
per_user = (
    df.groupby(["user_id", "name", "plan"])
    .agg(total_focus_minutes=("focus_minutes", "sum"),
         avg_focus_minutes=("focus_minutes", "mean"),
         sessions=("focus_minutes", "count"))
    .reset_index()
)
per_user["engagement"] = pd.cut(
    per_user["avg_focus_minutes"],
    bins=[0, 30, 60, float("inf")],
    labels=["low", "medium", "high"],
)

print("\nPer-user summary with engagement label:")
print(per_user.sort_values("total_focus_minutes", ascending=False))

# Filter down to just the users worth flagging for a "highly engaged" report
highly_engaged = per_user[per_user["engagement"] == "high"]
print("\nHighly engaged users:")
print(highly_engaged[["name", "plan", "avg_focus_minutes"]])

engine.dispose()
