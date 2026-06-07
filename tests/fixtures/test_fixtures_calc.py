# test_fixtures_basic_1

import pytest

from source.calculator import Calculator


@pytest.fixture(name="calculator")
def calculator_fixture():
    """Fixture that returns an instance of the Calculator class"""
    return Calculator()


def test_add(calculator):
    """Test the add method of the Calculator class"""

    assert calculator.add(2, 3) == 5


@pytest.mark.skip(reason="Not implemented yet")
def test_subtract(calculator):
    """Test the subtract method of the Calculator class"""

    assert calculator.subtract(5, 2) == 3


@pytest.mark.slow
def test_multiply(calculator):
    """Test the multiply method of the Calculator class"""

    assert calculator.multiply(4, 3) == 12


def test_divide(calculator):
    """Test the divide method of the Calculator class"""
    assert calculator.divide(6, 2) == 3


@pytest.mark.slow
def test_divide_by_zero(calculator):
    """Test the divide method of the Calculator class"""
    with pytest.raises(ZeroDivisionError):
        calculator.divide(5, 0)
