# Pandas Data Manipulation Reflection

## Research: how Pandas is used in data analytics

I learned that Pandas is built around the DataFrame, a table like structure where each column can hold a different data type, similar to a spreadsheet but built for code. I found it's the standard tool for loading data (from CSV, JSON, SQL, and more), cleaning it, reshaping it, and summarising it, all in a few lines rather than writing manual loops. What stood out to me is that most of a data analyst's day to day work, filtering rows, grouping and aggregating, joining separate tables together, and fixing messy or missing values, is exactly what Pandas is built for, which is why it comes up in basically every practical data task I've read about rather than staying a niche tool.

## Task notes

I built a practice script (`pandas_practice.py`) covering the full set of tasks: I loaded a sample usage dataset into a DataFrame, filtered and sorted rows, aggregated with `groupby` and `pivot_table`, joined two tables with `merge`, and cleaned the data with `replace()` (fixing an invalid negative value) and `fillna()` (filling a missing value with the column mean). I ran all of it end to end and confirmed it worked correctly.

## Reflection

**What are the advantages of using Pandas for data manipulation?**

For me, the biggest one is how much it replaces manual looping. If I wanted "average focus minutes per user" without Pandas, I'd have to write a loop, track totals and counts per user manually, and handle edge cases like missing values by hand. In Pandas I can do it in one line, `df.groupby("user_id")["focus_minutes"].mean()`, and it already handles things like missing values sensibly by default. I also like that it keeps the data in a consistent tabular structure throughout, so filtering, sorting, grouping, and joining all work the same predictable way regardless of what the underlying data actually is.

**How do you filter and aggregate data in Pandas?**

I filter using boolean conditions inside square brackets, like `df[df["focus_minutes"] > 60]`, which returns only the rows where that condition is true. For aggregating, I mainly use `groupby()`, splitting the data into groups (like by user or by device) and then applying a summary function like `.mean()` or `.sum()` to each group. I also used `pivot_table()`, which does something similar but lays the result out as a proper table, grouping by two dimensions at once (I used user and device), which I found easier to read than a grouped series when there are two categories at play.

**What techniques help handle missing or incorrect data?**

I start with `isnull().sum()` to actually see where the gaps are before doing anything about them. I use `replace()` for values that are technically present but wrong, in my case a negative number of focus minutes, which isn't missing data, it's invalid data I needed to correct first. I use `fillna()` for genuinely missing values, and I filled with the column mean in my case since dropping the whole row would have lost the other real data (like `sessions_completed`) for that row. I'd reach for `dropna()` instead when a value truly can't be filled or estimated reasonably, since it's better to drop the row than fill it with something misleading.

**How would Pandas be useful for analysing Focus Bear's user activity data?**

I can see the exact operations from this practice script mapping directly onto real usage data: I'd use `groupby` to compare average focus time or session counts across user segments (device type, plan, and so on), `pivot_table` to see two factors at once (like plan type against device), `merge` to join usage data with a separate users or subscriptions table (which is exactly what I practiced, combining session data with plan type), and `fillna`/`replace` to handle the kind of messy real world data I'd expect at scale, missed syncs, invalid entries, or gaps from users who didn't use the app on a given day.
