import pytest

from source.shopping_cart import ShoppingCart


@pytest.fixture(name="filled_cart", scope="class")
def pre_filled_cart_fixture():
    """Fixture that returns a pre-filled instance of the ShoppingCart class"""
    cart = ShoppingCart()
    cart.add_item("Apple", 1.5)
    cart.add_item("Banana", 2.5)
    yield cart


@pytest.fixture(name="empty_cart", scope="module")
def empty_cart_fixture():
    """Fixture that returns an empty instance of the ShoppingCart class"""
    yield ShoppingCart()


class TestScopeShoppingCart:
    def test_add_item(self, filled_cart):
        """Test the total and item added to the shopping cart"""
        filled_cart.add_item("Peach", 3.5)
        assert filled_cart.get_total() == 7.5
        assert filled_cart.item_count() == 3

    def test_add_extra_items(self, filled_cart):
        """Test the total and item added to the shopping cart"""
        assert filled_cart.item_count() == 3
        filled_cart.add_item("Blueberries", 2.0)
        assert filled_cart.item_count() == 4
        assert filled_cart.get_total() == 9.5
