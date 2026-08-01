# Refactored with clear, meaningful names (after refactor) - issue #42

def find_users_over_threshold(users, minutes_threshold):
    """Return (name, minutes_over_threshold) for users who exceeded the threshold."""
    users_over_threshold = []
    for user in users:
        if user["focus_minutes"] > minutes_threshold:
            clean_name = user["username"].strip().title()
            minutes_over = user["focus_minutes"] - minutes_threshold
            users_over_threshold.append((clean_name, minutes_over))
    return users_over_threshold

users = [
    {"username": "  koushik  ", "focus_minutes": 90},
    {"username": "priya", "focus_minutes": 45},
    {"username": "sam", "focus_minutes": 120},
]

print(find_users_over_threshold(users, minutes_threshold=60))
