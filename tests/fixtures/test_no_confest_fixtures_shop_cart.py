"""
Docstring for tests.test_shopping_cart
"""

import pytest

from source.shopping_cart import ShoppingCart


@pytest.fixture(name="cart")
# "cart" is the name of the fixture defined below,
# it will be passed as an argument to the test function
def shopping_cart_fixture():
    """Fixture that returns an instance of the ShoppingCart class"""
    return ShoppingCart()


@pytest.fixture(name="pre_filled_cart")
def pre_filled_cart_fixture(cart):
    """Fixture that returns a pre-filled instance of the ShoppingCart class"""
    cart.add_item("Apple", 1.5)
    cart.add_item("Banana", 2.5)
    return cart


def test_add_item(cart):
    """Test adding items to the shopping cart"""
    cart.add_item("Apple", 1.5)
    assert cart.item_count() == 1
    cart.add_item("Banana", 2.5)
    assert cart.item_count() == 2


def test_remove_item(cart):
    """Test removing items from the shopping cart"""
    cart.add_item("Apple", 1.5)
    cart.add_item("Banana", 2.5)
    cart.remove_item({"item": "Apple", "price": 1.5})
    assert cart.item_count() == 1
