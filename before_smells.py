# Code smells demo - BEFORE (issue #49)

# --- Smell 1: Magic Numbers & Strings ---
def calculate_late_fee(days_late):
    return days_late * 2.5  # what is 2.5? no context

# --- Smell 2: Long Functions ---
def process_signup(name, email, focus_minutes_goal):
    clean_name = name.strip().title()
    if "@" not in email or "." not in email:
        valid_email = False
    else:
        valid_email = True
    if focus_minutes_goal < 15:
        focus_minutes_goal = 15
    if focus_minutes_goal > 480:
        focus_minutes_goal = 480
    welcome_message = f"Welcome, {clean_name}!"
    plan_message = f"Your daily goal is {focus_minutes_goal} minutes."
    if valid_email:
        send_status = f"Confirmation sent to {email}"
    else:
        send_status = "Invalid email, confirmation not sent"
    full_message = welcome_message + " " + plan_message + " " + send_status
    return full_message

# --- Smell 3: Duplicate Code ---
def get_desktop_users(users):
    result = []
    for u in users:
        if u["device"] == "desktop":
            result.append(u["name"].strip().title())
    return result

def get_mobile_users(users):
    result = []
    for u in users:
        if u["device"] == "mobile":
            result.append(u["name"].strip().title())
    return result

# --- Smell 4: Large Class (God Object) ---
class UserManager:
    def __init__(self):
        self.users = []
    def add_user(self, name):
        self.users.append(name)
    def send_email(self, user, message):
        print(f"Emailing {user}: {message}")
    def calculate_billing(self, user, amount):
        return amount * 1.1
    def generate_pdf_report(self, user):
        return f"PDF report for {user}"
    def log_analytics_event(self, event):
        print(f"Logging: {event}")

# --- Smell 5: Deeply Nested Conditionals ---
def get_tier(minutes):
    if minutes is not None:
        if minutes > 0:
            if minutes >= 120:
                return "power"
            else:
                if minutes >= 60:
                    return "great"
                else:
                    return "good"
    return "none"

# --- Smell 6: Commented-Out Code ---
def get_greeting(name):
    # old_greeting = "Hi " + name
    # return old_greeting
    # print("debug: " + name)
    return f"Hello, {name}!"

# --- Smell 7: Inconsistent Naming ---
def calc(u, x):
    tempVal = u["focus_minutes"]
    Result = tempVal - x
    return Result
