# Connecting Python & Pandas to a SQL Database

## Tasks

Wrote [python_sql_query.py](python_sql_query.py), a standalone script that connects to the local PostgreSQL database with `psycopg` (v3) via a SQLAlchemy engine, runs a SQL query joining `users` and `focus_sessions` (the same tables seeded in issue #15), and loads the result straight into a Pandas DataFrame with `pandas.read_sql_query()`. From there it transforms the data in Pandas: a per-user rollup of total/average focus minutes, a derived `engagement` label (`low`/`medium`/`high`) built with `pd.cut()`, and a filtered view of just the highly engaged users, the kind of thing that would feed directly into an automated report.

## Reflection

**Why is it useful to query databases directly from Python instead of using a SQL client?**

Querying from Python means the result plugs straight into the rest of the pipeline, no manual step of exporting a CSV from a SQL client and re-importing it. It also makes the whole process repeatable and automatable: the same script can be scheduled to run daily, parameterised (different date ranges, different users), or chained into further transformations and a report or chart, none of which a one-off query typed into a SQL client naturally supports. It also keeps the query itself under version control alongside the analysis that uses it, so the two don't drift apart the way a saved SQL client query and a separate analysis script easily could.

**How does `psycopg` differ from `psycopg2`?**

`psycopg` (sometimes called psycopg3) is a from-scratch rewrite of `psycopg2`, not just a version bump. The two headline differences that mattered here: `psycopg` has native support for async/await (`psycopg2` doesn't), and it ships a much more direct SQLAlchemy integration through the `postgresql+psycopg://` dialect, which is what let `pandas.read_sql_query()` run without the "unsupported DBAPI2 connection" warning that showed up in issue #15's notebook using raw `psycopg2`. `psycopg` also has a cleaner connection pooling story (a separate `psycopg_pool` package) and better type adaptation between Python and Postgres types out of the box. Day-to-day query syntax (`cursor.execute`, parameterised queries with `%s` placeholders) is nearly identical, so switching between them for basic usage is a small change.

**How can Pandas help with post-query data transformation?**

Once the query result is a DataFrame, transformations that would need extra SQL (or a second query) become one-liners: `groupby().agg()` for per-user rollups, `pd.cut()` to bucket a continuous value like average focus minutes into engagement tiers, boolean filtering to isolate a subset like highly engaged users. Because it's all in memory, these can be layered and iterated on quickly, tweaking the bucket thresholds or adding another derived column doesn't mean rewriting and re-running the SQL, just rerunning a cell or a few lines of Pandas.

**How could this integration be used to generate automated reports for Focus Bear?**

A scheduled script (cron, a task runner, or an Airflow-style pipeline) could run this same query-then-transform pattern daily: pull the latest session data with `psycopg`/Pandas, compute the same kind of engagement summary, and then either write it to a report table, render it as a chart, or email/Slack a summary, all without anyone manually running a query. Because the connection and query logic live in a plain Python script rather than a notebook someone has to open and re-run, it's straightforward to wire into whatever scheduling system Focus Bear already uses for other automated jobs.
