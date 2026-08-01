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
