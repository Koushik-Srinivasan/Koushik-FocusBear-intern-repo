# Refactored into small, single-purpose functions - issue #43

def is_valid_user(user):
    """A user record is valid if it has both a name and a focus_minutes field."""
    return "name" in user and "focus_minutes" in user


def clean_focus_minutes(minutes):
    """Normalize focus minutes: treat missing/negative values as 0, round the rest."""
    if minutes is None or minutes < 0:
        return 0
    return round(minutes, 1)


def clean_name(name):
    """Trim whitespace and standardize capitalization."""
    return name.strip().title()


def calculate_daily_average(weekly_minutes):
    """Average minutes per day over a 7 day week."""
    return round(weekly_minutes / 7, 1) if weekly_minutes else 0


def format_user_line(name, minutes, daily_average):
    """Build the single summary line for one user."""
    status = "Active" if minutes > 0 else "Inactive"
    return f"{name}: {status}, {minutes} mins this week ({daily_average} mins/day avg)"


def build_summary_line(active_count, total_minutes):
    """Build the final totals line for the report."""
    return f"Total active users: {active_count}, Total minutes: {total_minutes}"


def process_user_report(users):
    """Coordinate the smaller functions to build the full report."""
    report_lines = []
    total_active = 0
    total_minutes = 0

    for user in users:
        if not is_valid_user(user):
            continue

        name = clean_name(user["name"])
        minutes = clean_focus_minutes(user["focus_minutes"])
        daily_average = calculate_daily_average(minutes)

        if minutes > 0:
            total_active += 1
            total_minutes += minutes

        report_lines.append(format_user_line(name, minutes, daily_average))

    report_lines.append("---")
    report_lines.append(build_summary_line(total_active, total_minutes))

    return "\n".join(report_lines)


sample_users = [
    {"name": "  koushik  ", "focus_minutes": 210},
    {"name": "priya", "focus_minutes": -5},
    {"name": "sam", "focus_minutes": None},
    {"name": "alex"},  # missing focus_minutes, should be skipped
]

print(process_user_report(sample_users))
