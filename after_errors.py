# Refactored with guard clauses and proper error handling (after) - issue #47

def calculate_average_focus_minutes(sessions):
    """
    Calculate the average focus_minutes across a list of session dicts.
    Raises clear, specific errors for invalid input instead of crashing
    with a confusing built-in exception.
    """
    if sessions is None:
        raise ValueError("sessions cannot be None, expected a list of session records.")

    if not isinstance(sessions, list):
        raise TypeError(f"sessions must be a list, got {type(sessions).__name__}.")

    if len(sessions) == 0:
        raise ValueError("sessions is empty, cannot calculate an average of zero sessions.")

    total = 0
    for i, session in enumerate(sessions):
        if "focus_minutes" not in session:
            raise KeyError(f"Session at index {i} is missing 'focus_minutes'.")
        if session["focus_minutes"] is None:
            raise ValueError(f"Session at index {i} has focus_minutes = None, expected a number.")
        total += session["focus_minutes"]

    return total / len(sessions)
