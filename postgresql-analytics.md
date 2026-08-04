# Using PostgreSQL for Analytics

## Tasks

I wrote [postgresql_analytics.sql](postgresql_analytics.sql) against my local `focusbear_dev` database (same `users`/`focus_sessions` tables from issue #15). First I bulked `focus_sessions` up to about 58,000 rows with `generate_series`, since the original 10-row seed was too small for the query planner to care about optimization one way or the other. Then I wrote a `JOIN` between `users` and `focus_sessions` with a `CASE` statement that buckets each session into `short`/`medium`/`long`, three window function queries (a running total, a `RANK()` of users by total focus minutes, and a 7-session moving average), and finally an `EXPLAIN ANALYZE` comparison before and after adding an index.

## Reflection

**What makes PostgreSQL a good choice for data analytics?**

Working through this, what stood out to me is how much analytical logic can live directly in the query instead of being pulled into application code. Window functions let me compute a running total and a moving average without a single loop in Python, `CASE` let me bucket data conditionally in the same query that fetched it, and indexing let me measure and then fix a real performance problem without changing a line of the query itself. PostgreSQL's JSON support (`jsonb`) is the piece I didn't get to use in this exercise, but from reading up on it, it's what would let something like a flexible per-session metadata field (say, arbitrary app settings at the time of a session) live in the same row without a rigid schema, while still being queryable and indexable. For Focus Bear's usage data specifically, that combination, structured relational data plus flexible JSON where it's genuinely needed, seems like a good fit.

**How do `JOIN` operations help in analyzing relational data?**

My `focus_sessions` table only stores a `user_id`, it doesn't know a user's name or plan. The `JOIN` to `users` is what lets me ask a question that spans both, like "how much did premium users focus, by name," in a single query instead of fetching sessions and users separately and stitching them together myself. That's the general pattern I saw across all my queries: the interesting analytical questions almost always span more than one table, and `JOIN` is what makes that a single round trip to the database instead of multiple queries and manual merging in application code.

**What are window functions, and how can they be used for user trend analysis?**

A window function computes a value across a set of related rows without collapsing them into one row the way `GROUP BY` does. In my running total query, every one of Alice's session rows is still there, but each one also carries the cumulative sum of her focus minutes up to that point. That's exactly the shape I'd want for a trend chart, one point per session, each with running context. My moving average query does something similar but bounded, averaging each row against the 6 before it, which smooths out day-to-day noise and would make a much more readable trend line than plotting raw session minutes. The `RANK()` query is a slightly different use, comparing users against each other rather than a user against their own history, which is the kind of thing a leaderboard or an "engagement tier" report would need.

**Why is query optimization important, and how does `EXPLAIN ANALYZE` help?**

I could actually see this rather than just take it on faith. Before adding an index on `focus_sessions.user_id`, `EXPLAIN ANALYZE` showed a `Seq Scan` that walked all ~58,000 rows to find the ~8,300 belonging to user 1, filtering out the other 41,657 by hand, taking 13.9ms. After I added `CREATE INDEX idx_focus_sessions_user_id ON focus_sessions (user_id)` and ran the identical query again, the plan switched to a `Bitmap Index Scan`, going straight to the matching rows instead of scanning everything, and the execution time dropped to 3.95ms, about 3.5x faster. At Focus Bear's actual scale, with far more than 58,000 session rows and this kind of query running repeatedly for reports or dashboards, that gap would only widen. `EXPLAIN ANALYZE` is what made the difference concrete instead of theoretical, it doesn't just guess at what a query will do, it actually runs it and reports the real plan and real timing, which is what let me confirm the index genuinely helped rather than assuming it would.
