# Identifying & Fixing Code Smells

I wrote `before_smells.py` containing one clear example of each of the 7 code smells, then refactored all of them in `after_smells.py`. I ran both files against the same inputs and confirmed identical output, so each fix changed the structure without changing behaviour.

## What code smells did I find and fix?

**1. Magic Numbers & Strings** — `calculate_late_fee` multiplied by `2.5` with no explanation of what that number means. Fixed by naming it `LATE_FEE_PER_DAY`, so the code and its intent are the same thing.

**2. Long Functions** — `process_signup` did name cleaning, email validation, goal clamping, and message building all in one function. Split into `clean_name`, `is_valid_email`, `clamp_focus_goal`, and a `build_signup_message` that just coordinates them.

**3. Duplicate Code** — `get_desktop_users` and `get_mobile_users` were identical except for one hardcoded string. Merged into one `get_users_by_device(users, device)` function.

**4. Large Class (God Object)** — `UserManager` handled users, email, billing, PDF reports, and analytics logging all in one class. Split into `UserRepository`, `EmailService`, `BillingService`, `ReportService`, and `AnalyticsLogger`, each with one responsibility.

**5. Deeply Nested Conditionals** — `get_tier` nested 3 levels of `if`/`else` to determine a tier. Flattened using early returns.

**6. Commented-Out Code** — `get_greeting` had 3 lines of dead, commented-out code sitting above the real return statement. Removed entirely, Git history already preserves old versions if they're ever needed again.

**7. Inconsistent Naming** — `calc(u, x)` used `tempVal` and `Result` (inconsistent casing, no real meaning). Renamed to `calculate_minutes_over_goal(user, goal_minutes)` with `focus_minutes` and `minutes_over_goal`.

## How did refactoring improve readability and maintainability?

Every fix followed the same underlying idea: make the code's structure match what it's actually doing. A named constant explains itself where a bare number can't. Small functions can be read and tested individually instead of needing the whole block held in your head. One shared function instead of two copies means a future change only needs to happen once. Splitting the god object means each class can be understood, tested, and changed without touching unrelated responsibilities.

## How can avoiding code smells make future debugging easier?

Most of these smells make debugging harder in the same way: they force you to read more code than necessary to understand or fix one specific thing. A magic number means you have to guess or go find where it's defined. Duplicate code means a bug fix might only get applied in one of the copies. A god object means a bug in billing logic could be hiding in a file that's 80% unrelated code. Fixing these smells doesn't just make the code look nicer, it directly narrows down how much code you need to read to find and safely fix a bug.
