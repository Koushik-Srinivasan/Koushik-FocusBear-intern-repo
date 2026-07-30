# Long, complex function example (before refactoring) - issue #43

def process_user_report(users):
    """Does everything at once: validation, cleaning, calculation, and formatting."""
    report_lines = []
    total_active = 0
    total_minutes = 0

    for user in users:
        # validation
        if "name" not in user or "focus_minutes" not in user:
            continue
        if user["focus_minutes"] is None:
            user["focus_minutes"] = 0
        if user["focus_minutes"] < 0:
            user["focus_minutes"] = 0

        # cleaning
        name = user["name"].strip().title()
        minutes = round(user["focus_minutes"], 1)

        # business logic
        is_active = minutes > 0
        if is_active:
            total_active += 1
            total_minutes += minutes

        status = "Active" if is_active else "Inactive"
        avg_per_day = round(minutes / 7, 1) if minutes else 0

        # formatting
        line = f"{name}: {status}, {minutes} mins this week ({avg_per_day} mins/day avg)"
        report_lines.append(line)

    summary = f"Total active users: {total_active}, Total minutes: {total_minutes}"
    report_lines.append("---")
    report_lines.append(summary)

    return "\n".join(report_lines)


sample_users = [
    {"name": "  koushik  ", "focus_minutes": 210},
    {"name": "priya", "focus_minutes": -5},
    {"name": "sam", "focus_minutes": None},
    {"name": "alex"},  # missing focus_minutes, should be skipped
]

print(process_user_report(sample_users))
