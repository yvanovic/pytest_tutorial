# test_fixtures_basic_1

# import pytest

from source.calculator import Calculator


def test_add():
    """Test the add method of the Calculator class"""
    calculator = Calculator()
    assert calculator.add(2, 3) == 5


def test_subtract():
    """Test the subtract method of the Calculator class"""
    calculator = Calculator()
    assert calculator.subtract(5, 2) == 3


def test_multiply():
    """Test the multiply method of the Calculator class"""
    calculator = Calculator()
    assert calculator.multiply(4, 3) == 12
