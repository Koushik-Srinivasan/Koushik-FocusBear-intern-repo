# Function with poor error handling (before) - issue #47

def calculate_average_focus_minutes(sessions):
    total = 0
    for s in sessions:
        total += s["focus_minutes"]
    return total / len(sessions)
