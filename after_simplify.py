# Simplified version (after refactor) - issue #45

def get_user_status_message(user):
    if not user or "focus_minutes" not in user:
        return "No data available."

    minutes = user["focus_minutes"]

    if minutes is None or minutes <= 0:
        return "No focus time yet today."
    if minutes >= 120:
        return "Power user today!"
    if minutes >= 60:
        return "Great session today!"
    return "Good start today!"


users = [
    {"focus_minutes": 150},
    {"focus_minutes": 75},
    {"focus_minutes": 30},
    {"focus_minutes": 0},
    {"focus_minutes": None},
    {},
    None,
]

for u in users:
    print(get_user_status_message(u))
