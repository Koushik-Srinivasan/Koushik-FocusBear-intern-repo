# SQL Basics Reflection

## Research: why SQL matters for analytics

SQL is the standard language for querying structured, table based data, and since Focus Bear's user data lives in PostgreSQL, it's how any real usage analysis would actually start, pulling and shaping the data before it even reaches a tool like Pandas.

## Task: practicing SELECT, WHERE, ORDER BY, GROUP BY, HAVING

I used SQLite (Python's built-in `sqlite3`) to build two small sample tables, `users` and `sessions`, and ran a series of real queries against them, all in `setup_and_queries.py`:

- **Simple SELECT**: `SELECT * FROM users` to retrieve all rows.
- **WHERE + ORDER BY**: filtered sessions over 40 minutes, sorted longest first.
- **GROUP BY**: summed total focus minutes per user.
- **GROUP BY + HAVING**: filtered down to only users whose total exceeded 60 minutes.
- **JOIN**: connected `sessions` back to `users` to show names and plan type alongside the totals.

I ran the script and confirmed every query returned the expected result, for example, Sam (premium) came out with 165 total minutes across two sessions, correctly the highest.

## Reflection

**How does SQL help in data analysis?**

It lets me ask a specific question directly against the data itself, "which users have over 60 minutes total," rather than pulling everything out first and filtering it manually elsewhere. Since Focus Bear's actual data lives in PostgreSQL, SQL is the natural first step before any of it reaches Python or Pandas.

**What is the difference between filtering (WHERE) and aggregation (GROUP BY)?**

`WHERE` filters individual rows before any grouping happens, keeping or discarding rows based on a condition (like `focus_minutes > 40`). `GROUP BY` collapses multiple rows into one summary row per group (like one row per user), so you can apply functions like `SUM()` or `COUNT()` across each group. `HAVING` is the equivalent of `WHERE` but for after grouping, filtering which groups appear based on the aggregated result (like keeping only users whose *total* exceeds 60), which is different from `WHERE`, since `WHERE` can't reference an aggregate like `SUM()` at all.

**How would I retrieve and analyze user activity data in Focus Bear's database?**

Based on this practice, I'd expect a real version to look very similar: join a sessions/usage table to the users table, group by user (or by device, or by plan), and use `HAVING` to isolate specific segments, like highly engaged users or users who've dropped off. The JOIN query I ran, combining session totals with plan type, is essentially a smaller version of exactly that kind of analysis.

**Why is learning SQL important even if I primarily use Python for analytics?**

Because the data usually starts in a database, not a CSV, so SQL is often the first and fastest step before anything reaches Pandas, pulling exactly the rows and aggregates needed rather than loading a whole table into Python and filtering there. Some things (like a `HAVING` filter on an aggregate) are also often more natural to express directly in SQL than to reconstruct in Pandas afterward.
