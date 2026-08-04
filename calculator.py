"""Function under test - issue #48."""

def calculate_order_total(quantity, unit_price, tax_multiplier):
    """Calculate order total, including tax and a bulk discount."""
    BULK_ORDER_THRESHOLD = 100
    BULK_DISCOUNT_RATE = 0.1

    subtotal = quantity * unit_price
    total_before_discount = subtotal * tax_multiplier

    if total_before_discount > BULK_ORDER_THRESHOLD:
        total_before_discount -= total_before_discount * BULK_DISCOUNT_RATE

    return round(total_before_discount, 2)
