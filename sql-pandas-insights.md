# Combining SQL + Pandas for Deeper Insights

## Tasks

Connected to a local PostgreSQL database using the same `.env`-based credentials from issue #14, then seeded two small tables, `users` and `focus_sessions`, shaped like Focus Bear usage data. Wrote a SQL query joining the two tables and loaded the result directly into a Pandas DataFrame with `pandas.read_sql_query()`, then did the deeper analysis in Pandas: per-user aggregates (total/average focus minutes, session counts), a pivot of focus minutes by device, and a plan-tier comparison built on top of the already-computed aggregate rather than re-querying the database. The full working example, with real executed output, is in [sql_pandas_insights_demo.ipynb](sql_pandas_insights_demo.ipynb).

## Reflection

**How can combining SQL and Pandas improve data analysis and reporting for Focus Bear?**

SQL is the right tool for the part it's already good at, filtering and joining rows close to where the data lives, so only the relevant subset (a specific user's sessions, a date range, a join across tables) ever crosses into Python instead of pulling entire tables into memory first. Pandas takes over for the part SQL is clumsy at, reshaping that result into multiple views, pivoting focus minutes by device, computing several aggregates at once, or feeding an already-computed summary into a second-level comparison, without writing increasingly nested SQL or re-hitting the database for each variation. For something like Focus Bear's usage reporting, that split means a report can start from one well-scoped query and then branch into several different summaries or charts entirely in Pandas, instead of writing a new SQL query for every cut of the data. It also keeps the heavier computation (aggregation across many rows) at the database layer where it's efficient, while the exploratory, ad-hoc parts of the analysis happen locally where iterating is fast.
