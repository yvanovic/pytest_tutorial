"""This module contains fixtures for testing the ShoppingCart class.
These fixtures can be used across multiple test files to provide a consistent setup
for testing the shopping cart functionality."""

import pytest
import requests

from source.shopping_cart import ShoppingCart

BASE_URL = "https://jsonplaceholder.typicode.com"


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


@pytest.fixture(scope="session")
def base_url():
    """Fixture that returns the base url for all tests"""
    return BASE_URL


@pytest.fixture(scope="session")
def api_session():
    """Fixture that returns the API session for all tests"""
    session = requests.Session()
    session.headers.update(
        {"Content-Type": "application/json", "Accept": "application/json"}
    )
    yield session
    session.close()
