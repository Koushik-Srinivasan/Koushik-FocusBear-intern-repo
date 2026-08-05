# Overly complex code example (before refactor) - issue #45

def get_user_status_message(user):
    if user is not None:
        if "focus_minutes" in user:
            if user["focus_minutes"] is not None:
                if user["focus_minutes"] > 0:
                    if user["focus_minutes"] >= 60:
                        if user["focus_minutes"] >= 120:
                            return "Power user today!"
                        else:
                            return "Great session today!"
                    else:
                        return "Good start today!"
                else:
                    return "No focus time yet today."
            else:
                return "No focus time yet today."
        else:
            return "No data available."
    else:
        return "No data available."


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
