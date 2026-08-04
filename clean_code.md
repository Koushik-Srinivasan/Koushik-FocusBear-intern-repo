# Clean Code: Comments & Documentation

## Research: best practices for comments and documentation

Comments should explain *why*, not *what*. Code already shows what it's doing, so a comment that just restates a line adds noise, not value. Comments earn their place explaining things code can't: a business rule, a workaround, a reason behind a non-obvious approach. Good naming often removes the need for a comment in the first place.

## Example: poorly commented code, rewritten

**Before** (comments just restate each line):

```python
def calc(a, b, c):
    # add a and b
    x = a + b
    # multiply x by c
    y = x * c
    # set discount to 0.1
    discount = 0.1
    # if y is greater than 100
    if y > 100:
        # subtract discount from y
        y = y - (y * discount)
    # return y
    return y
```

Every comment repeats what the code already says, and unclear names (`calc`, `a`, `b`, `c`) mean it's still unclear what this actually calculates.

**After** (renamed, comments only where they add real information):

```python
BULK_ORDER_THRESHOLD = 100
BULK_DISCOUNT_RATE = 0.1

def calculate_order_total(quantity, unit_price, tax_multiplier):
    """Calculate order total, including tax and a bulk discount."""
    subtotal = quantity + unit_price
    total_before_discount = subtotal * tax_multiplier

    # Bulk discount is a business rule from the pricing team, not obvious from the math alone.
    if total_before_discount > BULK_ORDER_THRESHOLD:
        total_before_discount -= total_before_discount * BULK_DISCOUNT_RATE

    return total_before_discount
```

Clear names made most line-by-line comments unnecessary. The one comment left explains something the code can't: that the threshold is a business decision, not an arbitrary number.

## Reflection

**When should I add comments?**

When code can't explain itself: a business rule, a workaround, a non-obvious design choice, or a docstring summarizing what a function does.

**When should I avoid comments and instead improve the code?**

When a comment only exists because the naming or structure is unclear. The fix there is renaming or restructuring, not documenting around confusing code. Test: if I fixed the naming, would the comment become unnecessary? If yes, fix the code instead.

---

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

---

# Naming Variables & Functions

## Research: naming best practices

A good name says what a thing *is* or what a function *does*, without needing to read the body to figure it out. Names should be specific rather than generic (`users_over_threshold`, not `r`), and functions are usually named as verbs (`find_users_over_threshold`) since they do something, while variables are named as nouns.

## Example: refactoring unclear names

**Before**, single-letter and abbreviated names hide what the function actually does:

```python
def calc(d, x):
    r = []
    for i in d:
        if i["t"] > x:
            n = i["u"].strip().title()
            v = i["t"] - x
            r.append((n, v))
    return r
```

Nothing here says what `calc` calculates, or what `d`, `x`, `t`, `u` actually represent, you'd have to trace through the logic just to guess.

**After**, same logic, clear names throughout:

```python
def find_users_over_threshold(users, minutes_threshold):
    """Return (name, minutes_over_threshold) for users who exceeded the threshold."""
    users_over_threshold = []
    for user in users:
        if user["focus_minutes"] > minutes_threshold:
            clean_name = user["username"].strip().title()
            minutes_over = user["focus_minutes"] - minutes_threshold
            users_over_threshold.append((clean_name, minutes_over))
    return users_over_threshold
```

Tested both, identical output. The function name alone now tells you what it does, no need to read the body first.

## Reflection

**What makes a good variable or function name?**

Specific enough to say what it holds or does without extra explanation, `minutes_threshold` over `x`, `find_users_over_threshold` over `calc`.

**What issues can arise from poorly named variables?**

Bugs hide more easily, since it's harder to spot when the wrong variable is used if `t` and `x` look interchangeable. It also slows down anyone reading the code later, including future me, since every line needs mental translation instead of just reading naturally.

**How did refactoring improve code readability?**

The refactored function reads almost like a sentence, "find users over threshold, using their focus minutes." No comments were even needed to explain what's happening, the names carry that on their own.

---

# Writing Unit Tests for Clean Code

## Research and setup

I chose PyTest since it's the standard testing framework for Python and has simple syntax, just `assert` statements, no boilerplate classes needed. I wrote 6 unit tests for `calculate_order_total()` (the function from the comments/documentation example earlier in this file), covering normal cases, an edge case at the exact discount threshold, rounding behaviour, and a genuine bug I found while testing.

I ran them with `pytest test_calculator.py -v`, all 6 passed.

## Reflection

**How do unit tests help keep code clean?**

Writing the tests forced me to actually think through edge cases I hadn't considered while writing the function itself, like what happens exactly at the threshold, or with a quantity of zero. Having tests also means I could refactor this function later and immediately know if I broke something, instead of only finding out when something looks wrong somewhere else much later.

**What issues did you find while testing?**

I found a real gap: the function doesn't validate for negative quantity or price, so `calculate_order_total(-5, 20, 1.0)` silently returns `-100.0` instead of raising an error. I wrote a test that documents this current behaviour rather than pretending it's correct, since that's an issue worth fixing (adding input validation) rather than something to just accept.
