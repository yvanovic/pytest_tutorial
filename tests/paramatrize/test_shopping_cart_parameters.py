"""Tests for shopping_cart_parameters.py"""

import pytest

# from source.shopping_cart import ShoppingCart

# @pytest.fixture(name="cart")
# def shopping_cart_fixture():
#     return ShoppingCart()


@pytest.mark.parametrize("invalid_percentage", [-10, -1, 101, 150])
def test_invalid_percentage(cart, invalid_percentage):
    """Test that an invalid percentage value raises an error"""
    with pytest.raises(ValueError):
        cart.apply_discount(invalid_percentage)


@pytest.mark.parametrize(
    "percentage, original_total, expected_total",
    [(50, 6, 3), (25, 10, 7.5)],
    ids=["50-percent", "25-percentage"],
)
def test_apply_discount_calculation(cart, percentage, original_total, expected_total):
    """Test that apply_discount(percentage) works correctly"""
    cart.add_item("Apple", original_total)

    discounted = cart.apply_discount(percentage)
    assert discounted == expected_total


@pytest.mark.parametrize("item, price", [("Apple", 1.5), ("Banana", 2.5)])
def test_add_item(cart, item, price):
    """Test adding an item to the shopping cart"""
    cart.add_item(item, price)
    assert cart.item_count() == 1


@pytest.mark.parametrize(
    "percent, expected_total",
    [
        (10, 3.6),
        (25, 3.0),
        (50, 2.0),
    ],
    ids=["10_percent", "25_percent", "50_percent"],
)
def test_apply_discount_on_cart(pre_filled_cart, percent, expected_total):
    """Test various discount percentages on a cart with items"""
    discounted = pre_filled_cart.apply_discount(percent)
    assert round(discounted, 4) == expected_total
