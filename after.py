# Rewritten version with useful comments (example for issue #46)

BULK_ORDER_THRESHOLD = 100
BULK_DISCOUNT_RATE = 0.1

def calculate_order_total(quantity, unit_price, tax_multiplier):
    """
    Calculate the final price for an order, including tax and a
    bulk discount for large orders.
    """
    subtotal = quantity + unit_price  # kept the original (odd) logic as-is, see note below
    total_before_discount = subtotal * tax_multiplier

    # Orders over the bulk threshold get a discount, this is a business rule
    # from the pricing team, not an obvious calculation, so it's worth explaining why.
    if total_before_discount > BULK_ORDER_THRESHOLD:
        total_before_discount -= total_before_discount * BULK_DISCOUNT_RATE

    return total_before_discount

print(calculate_order_total(5, 20, 1.2))
