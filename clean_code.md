# Clean Code: Comments & Documentation

## Research: best practices for comments and documentation

The general principle that comes up again and again is that comments should explain *why*, not *what*. Code already shows what it's doing, line by line, so a comment that just restates the line in English adds noise rather than value. Comments earn their place when they explain a decision that isn't obvious from the code itself: a business rule, a workaround for a bug, a reason a "weird looking" approach was chosen over the obvious one. Good naming (functions, variables) does a lot of the work that comments would otherwise need to do, if a function is named clearly, you often don't need a comment above it explaining what it does.

For documentation more broadly (README files, docstrings, setup guides), the goal is to answer the questions a new person would actually have: what does this do, how do I run it, what do I need to know before changing it. Docstrings on functions are useful because they show up in tooltips/autocomplete, so they help even without opening the source file.

## Example: poorly commented code, rewritten

**Before** (comments just restate each line, adding no real information):

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

Every comment here just repeats what the line of code already says. Worse, the function and variable names (`calc`, `a`, `b`, `c`, `x`, `y`) give no indication of what this is actually calculating, so even with the comments, it's unclear what real world thing this function represents.

**After** (renamed for clarity, comments only where they add real information):

```python
BULK_ORDER_THRESHOLD = 100
BULK_DISCOUNT_RATE = 0.1

def calculate_order_total(quantity, unit_price, tax_multiplier):
    """
    Calculate the final price for an order, including tax and a
    bulk discount for large orders.
    """
    subtotal = quantity + unit_price
    total_before_discount = subtotal * tax_multiplier

    # Orders over the bulk threshold get a discount, this is a business rule
    # from the pricing team, not an obvious calculation, so it's worth explaining why.
    if total_before_discount > BULK_ORDER_THRESHOLD:
        total_before_discount -= total_before_discount * BULK_DISCOUNT_RATE

    return total_before_discount
```

Most of the line by line comments disappeared entirely, because the new names (`calculate_order_total`, `quantity`, `unit_price`, `subtotal`) already make each line self explanatory. The one comment that remains explains something the code itself can't, that the discount threshold is a business decision from another team, not just an arbitrary number someone picked, which is exactly the kind of thing a comment should be for.

## Reflection

**When should I add comments?**

When the code can't explain itself, specifically: a business rule or requirement that isn't obvious from the logic alone, a workaround for a bug or limitation in another system, a non obvious reason a particular approach was chosen over a simpler seeming one, or a warning about something that looks safe to change but isn't. Comments are also worth it above a function as a docstring, summarizing what it does and why it exists, even if the body is fairly readable, since that shows up in tooltips and saves someone from having to open the file at all.

**When should I avoid comments and instead improve the code?**

When the comment only exists because the code itself is unclear, unclear naming, a function doing too many unrelated things, or deeply nested logic that's hard to follow. In those cases the actual fix is to rename things properly, split the function into smaller well named pieces, or restructure the logic, not to add an explanation on top of confusing code. A comment that just translates code into English line by line is almost always a sign the code should be rewritten to be clearer instead. The real test is: if I improved the naming and structure, would this comment become unnecessary? If yes, fix the code instead of documenting around it.

---

# Writing Small, Focused Functions

## Research: best practices for small, single-purpose functions

The common principle is that a function should do one thing, and its name should be able to say exactly what that one thing is. If describing what a function does requires the word "and" (validates and cleans and calculates and formats), that's usually a sign it should be split into separate functions. Small functions are also easier to test in isolation, easier to reuse elsewhere, and easier to read top to bottom since each one fits in your head at once rather than needing to track several unrelated concerns through one long block.

## Example: refactoring a long function

**Before** (one function doing validation, cleaning, calculation, and formatting all at once):

```python
def process_user_report(users):
    report_lines = []
    total_active = 0
    total_minutes = 0

    for user in users:
        if "name" not in user or "focus_minutes" not in user:
            continue
        if user["focus_minutes"] is None:
            user["focus_minutes"] = 0
        if user["focus_minutes"] < 0:
            user["focus_minutes"] = 0

        name = user["name"].strip().title()
        minutes = round(user["focus_minutes"], 1)

        is_active = minutes > 0
        if is_active:
            total_active += 1
            total_minutes += minutes

        status = "Active" if is_active else "Inactive"
        avg_per_day = round(minutes / 7, 1) if minutes else 0

        line = f"{name}: {status}, {minutes} mins this week ({avg_per_day} mins/day avg)"
        report_lines.append(line)

    summary = f"Total active users: {total_active}, Total minutes: {total_minutes}"
    report_lines.append("---")
    report_lines.append(summary)

    return "\n".join(report_lines)
```

This one function is responsible for deciding what makes a user record valid, cleaning both the name and the minutes, calculating an average, deciding active/inactive status, and formatting two different kinds of output lines. Reading it top to bottom means holding all of that in your head simultaneously to understand any one part of it.

**After** (split into small, single-purpose functions):

```python
def is_valid_user(user):
    return "name" in user and "focus_minutes" in user

def clean_focus_minutes(minutes):
    if minutes is None or minutes < 0:
        return 0
    return round(minutes, 1)

def clean_name(name):
    return name.strip().title()

def calculate_daily_average(weekly_minutes):
    return round(weekly_minutes / 7, 1) if weekly_minutes else 0

def format_user_line(name, minutes, daily_average):
    status = "Active" if minutes > 0 else "Inactive"
    return f"{name}: {status}, {minutes} mins this week ({daily_average} mins/day avg)"

def build_summary_line(active_count, total_minutes):
    return f"Total active users: {active_count}, Total minutes: {total_minutes}"

def process_user_report(users):
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
```

I ran both versions against the same sample data and confirmed they produce identical output, so the refactor changed the structure without changing the behaviour.

## Reflection

**Why is breaking down functions beneficial?**

Each small function's name already says what it does, so I don't need to read the body of `process_user_report` to understand its shape. Each piece is also easier to test on its own, like testing `clean_focus_minutes` for negative numbers without needing a full user list.

**How did refactoring improve the structure of the code?**

The original function mixed four concerns (validation, cleaning, calculation, formatting) in one block, so a bug in any one meant reading through all of them. After refactoring, `process_user_report` reads like a table of contents, one line per step, with the logic tucked into its own named function elsewhere.
