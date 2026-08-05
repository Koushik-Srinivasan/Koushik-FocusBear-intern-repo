# Code smells demo - AFTER refactoring (issue #49)

# --- Fix 1: Magic Numbers & Strings -> named constant ---
LATE_FEE_PER_DAY = 2.5

def calculate_late_fee(days_late):
    return days_late * LATE_FEE_PER_DAY


# --- Fix 2: Long Function -> split into small, single-purpose functions ---
MIN_FOCUS_GOAL_MINUTES = 15
MAX_FOCUS_GOAL_MINUTES = 480

def clean_name(name):
    return name.strip().title()

def is_valid_email(email):
    return "@" in email and "." in email

def clamp_focus_goal(minutes):
    return max(MIN_FOCUS_GOAL_MINUTES, min(minutes, MAX_FOCUS_GOAL_MINUTES))

def build_signup_message(name, email, focus_minutes_goal):
    name = clean_name(name)
    focus_minutes_goal = clamp_focus_goal(focus_minutes_goal)
    email_status = f"Confirmation sent to {email}" if is_valid_email(email) else "Invalid email, confirmation not sent"
    return f"Welcome, {name}! Your daily goal is {focus_minutes_goal} minutes. {email_status}"


# --- Fix 3: Duplicate Code -> one function, parameterized ---
def get_users_by_device(users, device):
    return [u["name"].strip().title() for u in users if u["device"] == device]


# --- Fix 4: Large Class (God Object) -> split by responsibility ---
class UserRepository:
    def __init__(self):
        self.users = []
    def add_user(self, name):
        self.users.append(name)

class EmailService:
    def send_email(self, user, message):
        print(f"Emailing {user}: {message}")

class BillingService:
    def calculate_billing(self, amount):
        return amount * 1.1

class ReportService:
    def generate_pdf_report(self, user):
        return f"PDF report for {user}"

class AnalyticsLogger:
    def log_event(self, event):
        print(f"Logging: {event}")


# --- Fix 5: Deeply Nested Conditionals -> early returns ---
def get_tier(minutes):
    if minutes is None or minutes <= 0:
        return "none"
    if minutes >= 120:
        return "power"
    if minutes >= 60:
        return "great"
    return "good"


# --- Fix 6: Commented-Out Code -> removed entirely (Git history keeps old versions) ---
def get_greeting(name):
    return f"Hello, {name}!"


# --- Fix 7: Inconsistent Naming -> clear, consistent names ---
def calculate_minutes_over_goal(user, goal_minutes):
    focus_minutes = user["focus_minutes"]
    minutes_over_goal = focus_minutes - goal_minutes
    return minutes_over_goal
