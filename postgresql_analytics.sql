-- Using PostgreSQL for Analytics (issue #17)
-- Builds on the users/focus_sessions tables seeded in issue #15, run against
-- the local focusbear_dev database.

-- ============================================================
-- Step 1: Bulk up focus_sessions so query optimization is meaningful
-- (the original 10-row seed is too small for the planner to care about an index)
-- ============================================================
INSERT INTO focus_sessions (user_id, session_date, focus_minutes, device)
SELECT
    (RANDOM() * 3 + 1)::INT AS user_id,
    DATE '2025-01-01' + (RANDOM() * 600)::INT AS session_date,
    (RANDOM() * 110 + 5)::INT AS focus_minutes,
    (ARRAY['desktop', 'mobile'])[FLOOR(RANDOM() * 2 + 1)] AS device
FROM generate_series(1, 50000);

-- ============================================================
-- Step 2: JOIN across tables + CASE for a conditional transformation
-- ============================================================
SELECT
    u.name,
    u.plan,
    s.session_date,
    s.focus_minutes,
    CASE
        WHEN s.focus_minutes < 20 THEN 'short'
        WHEN s.focus_minutes < 60 THEN 'medium'
        ELSE 'long'
    END AS session_length
FROM focus_sessions s
JOIN users u ON u.user_id = s.user_id
ORDER BY s.session_date
LIMIT 10;

-- ============================================================
-- Step 3: Window functions for user trend analysis
-- ============================================================

-- Running total of focus minutes per user, ordered by date
SELECT
    u.name,
    s.session_date,
    s.focus_minutes,
    SUM(s.focus_minutes) OVER (
        PARTITION BY u.user_id ORDER BY s.session_date
    ) AS running_total_minutes
FROM focus_sessions s
JOIN users u ON u.user_id = s.user_id
WHERE u.name = 'Alice'
ORDER BY s.session_date
LIMIT 10;

-- Rank users by total focus minutes
SELECT
    u.name,
    SUM(s.focus_minutes) AS total_minutes,
    RANK() OVER (ORDER BY SUM(s.focus_minutes) DESC) AS focus_rank
FROM focus_sessions s
JOIN users u ON u.user_id = s.user_id
GROUP BY u.name;

-- 7-session moving average of focus_minutes per user
SELECT
    u.name,
    s.session_date,
    s.focus_minutes,
    ROUND(AVG(s.focus_minutes) OVER (
        PARTITION BY u.user_id
        ORDER BY s.session_date
        ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
    ), 1) AS moving_avg_7
FROM focus_sessions s
JOIN users u ON u.user_id = s.user_id
WHERE u.name = 'Alice'
ORDER BY s.session_date
LIMIT 10;

-- ============================================================
-- Step 4: EXPLAIN ANALYZE before optimization (no index on user_id)
-- ============================================================
EXPLAIN ANALYZE
SELECT u.name, COUNT(*), SUM(s.focus_minutes)
FROM focus_sessions s
JOIN users u ON u.user_id = s.user_id
WHERE s.user_id = 1
GROUP BY u.name;

-- ============================================================
-- Step 5: Add an index and re-run the same query
-- ============================================================
CREATE INDEX idx_focus_sessions_user_id ON focus_sessions (user_id);

EXPLAIN ANALYZE
SELECT u.name, COUNT(*), SUM(s.focus_minutes)
FROM focus_sessions s
JOIN users u ON u.user_id = s.user_id
WHERE s.user_id = 1
GROUP BY u.name;
