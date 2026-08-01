# Duplicated code example (before DRY refactor) - issue #44

def send_welcome_email(user_name, user_email):
    print(f"Connecting to email server...")
    print(f"Preparing email for {user_email}")
    subject = "Welcome to Focus Bear!"
    body = f"Hi {user_name}, welcome aboard! We're glad to have you."
    print(f"Subject: {subject}")
    print(f"Body: {body}")
    print(f"Email sent to {user_email}")

def send_reminder_email(user_name, user_email):
    print(f"Connecting to email server...")
    print(f"Preparing email for {user_email}")
    subject = "Don't forget your daily routine!"
    body = f"Hi {user_name}, you haven't completed today's routine yet."
    print(f"Subject: {subject}")
    print(f"Body: {body}")
    print(f"Email sent to {user_email}")

def send_streak_broken_email(user_name, user_email):
    print(f"Connecting to email server...")
    print(f"Preparing email for {user_email}")
    subject = "Your streak was reset"
    body = f"Hi {user_name}, your streak was reset, but you can start a new one today."
    print(f"Subject: {subject}")
    print(f"Body: {body}")
    print(f"Email sent to {user_email}")

send_welcome_email("Koushik", "koushik@example.com")
send_reminder_email("Koushik", "koushik@example.com")
send_streak_broken_email("Koushik", "koushik@example.com")
