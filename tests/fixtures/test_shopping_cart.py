"""
Docstring for tests.test_shopping_cart
"""

import pytest

from source.shopping_cart import ShoppingCart


# @pytest.fixture(name="cart")
# # "cart" is the name of the fixture defined below,
# # it will be passed as an argument to the test function
# def shopping_cart_fixture():
#     """Fixture that returns an instance of the ShoppingCart class"""
#     return ShoppingCart()
#
#
# @pytest.fixture(name="pre_filled_cart")
# def pre_filled_cart_fixture(cart):
#     """Fixture that returns a pre-filled instance of the ShoppingCart class"""
#     cart.add_item("Apple", 1.5)
#     cart.add_item("Banana", 2.5)
#     return cart


def test_add_item(cart):
    """Test adding items to the shopping cart"""
    cart.add_item("Pear", 1.0)
    assert cart.item_count() == 1
    cart.add_item("Orange", 1.25)
    assert cart.item_count() == 2


def test_get_total(cart):
    """Test calculating the total price of items in the shopping cart"""
    cart.add_item("Milk", 2.0)
    cart.add_item("Bread", 1.5)
    assert cart.get_total() == 3.5


def test_item_count(pre_filled_cart):
    """Test counting the number of items in the shopping cart"""
    pre_filled_cart.add_item("Eggs", 3.0)
    assert pre_filled_cart.item_count() == 3


def test_empty_cart(cart):
    """Test the total and item count for an empty shopping cart"""
    assert cart.get_total() == 0
    assert cart.item_count() == 0


def test_remove_item(pre_filled_cart):
    """Test removing an item from the shopping cart"""
    item_to_remove = {"item": "Apple", "price": 1.5}
    pre_filled_cart.remove_item(item_to_remove)
    assert pre_filled_cart.item_count() == 1
    assert pre_filled_cart.get_total() == 2.5


def test_remove_nonexistent_item(cart):
    """Test removing an item that does not exist in the shopping cart"""
    item_to_remove = {"item": "Mango", "price": 1}
    with pytest.raises(ValueError):
        cart.remove_item(item_to_remove)
    assert cart.item_count() == 0


def test_clear(pre_filled_cart):
    """Test clearing items in the shopping cart"""
    pre_filled_cart.add_item("Mango", 3.5)
    assert pre_filled_cart.item_count() == 3
    pre_filled_cart.clear()
    assert pre_filled_cart.item_count() == 0


def test_discount(pre_filled_cart):
    """Test discounting items in the shopping cart"""
    pre_filled_cart.add_item("Mango", 6)
    assert pre_filled_cart.item_count() == 3
    assert pre_filled_cart.get_total() == 10
    discount = pre_filled_cart.apply_discount(50)
    assert discount == 5

def test_apply_discount_no_discount(pre_filled_cart):
    """Test applying discount without discount"""
    pre_filled_cart.add_item("Mango", 6)
    original_total = pre_filled_cart.get_total()
    discount = pre_filled_cart.apply_discount(0)
    assert discount == original_total

def test_apply_discount_invalid_percentage(cart):
    """Test applying discount with an invalid percentage"""
    with pytest.raises(ValueError):
        cart.apply_discount(101)
    assert cart.item_count() == 0