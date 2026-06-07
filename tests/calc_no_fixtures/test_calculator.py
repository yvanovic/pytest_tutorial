# test_fixtures_basic_1
import pytest

from source.calculator import Calculator


class TestCalculator:

    @staticmethod
    def test_add():
        """Test the add method of the Calculator class"""
        calculator = Calculator()
        assert calculator.add(2, 3) == 5

    @staticmethod
    def test_subtract():
        """Test the subtract method of the Calculator class"""
        calculator = Calculator()
        assert calculator.subtract(5, 2) == 3

    @staticmethod
    def test_multiply():
        """Test the multiply method of the Calculator class"""
        calculator = Calculator()
        assert calculator.multiply(4, 3) == 12

    @staticmethod
    def test_divide():
        """Test the divide method of the Calculator class"""
        calculator = Calculator()
        assert calculator.divide(6, 2) == 3

    @staticmethod
    def test_divide_by_zero():
        """Test the divide_by_zero method of the Calculator class"""
        calculator = Calculator()
        with pytest.raises(ZeroDivisionError):
            calculator.divide(5, 0)
