"""Unit tests for calculate_order_total - issue #48."""

from calculator import calculate_order_total


def test_small_order_no_discount():
    # Small order, total stays under the bulk threshold, no discount applied
    result = calculate_order_total(quantity=2, unit_price=10, tax_multiplier=1.0)
    assert result == 20.0


def test_large_order_gets_bulk_discount():
    # Order total exceeds the bulk threshold (100), so a 10% discount applies
    result = calculate_order_total(quantity=5, unit_price=20, tax_multiplier=1.2)
    # subtotal = 100, after tax = 120, over threshold -> 120 - 12 = 108
    assert result == 108.0


def test_zero_quantity_returns_zero():
    result = calculate_order_total(quantity=0, unit_price=50, tax_multiplier=1.1)
    assert result == 0.0


def test_result_is_rounded_to_two_decimals():
    result = calculate_order_total(quantity=3, unit_price=9.995, tax_multiplier=1.0)
    # 3 * 9.995 = 29.985, should round to 29.99 or 29.98 depending on rounding rule
    assert result == round(3 * 9.995, 2)


def test_exact_threshold_does_not_trigger_discount():
    # total_before_discount exactly equals 100, discount only applies when STRICTLY greater
    result = calculate_order_total(quantity=10, unit_price=10, tax_multiplier=1.0)
    assert result == 100.0


def test_negative_quantity_currently_not_validated():
    # This documents a real gap found while testing: the function doesn't
    # validate for negative inputs, so it silently returns a negative total
    # instead of raising an error. Marked as a known issue, not a passing
    # spec, since the current behaviour probably shouldn't be relied on.
    result = calculate_order_total(quantity=-5, unit_price=20, tax_multiplier=1.0)
    assert result == -100.0  # documents current (questionable) behaviour
