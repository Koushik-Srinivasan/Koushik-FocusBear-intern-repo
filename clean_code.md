# Avoiding Code Duplication (DRY)

## Research: DRY principle

"Don't Repeat Yourself" means each piece of logic should exist in one place, not copy-pasted across multiple functions. Duplication isn't just extra typing, it's extra risk: if the logic needs to change, every copy needs updating, and it's easy to miss one.

## Example: refactoring duplicated code

**Before**, three email functions each repeated the same connection/send logic:

```python
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
```

(a third, `send_streak_broken_email`, repeated the same pattern again)

**After**, the shared logic was pulled into one `send_email` function, and each specific function just supplies its own subject/body:

```python
def send_email(user_name, user_email, subject, body):
    print(f"Connecting to email server...")
    print(f"Preparing email for {user_email}")
    print(f"Subject: {subject}")
    print(f"Body: {body}")
    print(f"Email sent to {user_email}")

def send_welcome_email(user_name, user_email):
    subject = "Welcome to Focus Bear!"
    body = f"Hi {user_name}, welcome aboard! We're glad to have you."
    send_email(user_name, user_email, subject, body)
```

Tested both versions, identical output.

## Reflection

**What were the issues with duplicated code?**

If the sending logic ever needed to change (say, adding an error check), it would need updating in three separate places, easy to miss one and leave an inconsistency behind.

**How did refactoring improve maintainability?**

Now there's exactly one place that knows how to send an email. Each specific function only holds what's actually unique to it, the subject and body, making the duplication and the real differences both easier to see at a glance.
