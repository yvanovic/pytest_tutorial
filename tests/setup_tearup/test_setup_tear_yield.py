# This test file demonstrates using a pytest fixture with yield
# to set up and tear down a shopping cart for testing.
"""
Docstring for tests.test_shopping_cart_yield
"""
import pytest

from source.shopping_cart import ShoppingCart


@pytest.fixture(name="cart")
def shopping_cart_fixture():
    """Fixture that creates a shopping cart, yields it for testing,
    and then clears it after the test"""
    print("\n 🛒 SETUP: Creating Shopping Cart ")
    cart = ShoppingCart()
    # This is where the tests function will run and receive the "cart" instance as an argument
    yield cart

    print(f"\n 🧹 TEARDOWN: Cart had {cart.item_count()} items, cleanup")
    cart.clear()


@pytest.fixture(name="pre_filled_cart")
def pre_filled_cart_fixture(cart):
    cart.add_item("Orange", 1.25)
    cart.add_item("Apple", 1.5)
    return cart


def test_add_items_setup(cart):
    """Test adding items to the shopping cart using the setup and teardown fixture"""
    cart.add_item("Pear", 1.0)
    assert cart.item_count() == 1
    cart.add_item("Orange", 1.25)
    assert cart.item_count() == 2


def test_empty_cart(cart):
    """Test the total and item count for an empty shopping cart"""
    assert cart.get_total() == 0
    assert cart.item_count() == 0


def test_remove_item(pre_filled_cart):
    """Test removing an item from the shopping cart"""
    pre_filled_cart.add_item("Mango", 1.5)
    assert pre_filled_cart.item_count() == 3
    pre_filled_cart.remove_item({"item": "Mango", "price": 1.5})
    assert pre_filled_cart.item_count() == 2
