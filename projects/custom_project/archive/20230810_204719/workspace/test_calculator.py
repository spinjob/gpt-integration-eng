import pytest
from calculator import Calculator

class TestCalculator:
    """Unit tests for the Calculator class."""

    @pytest.mark.parametrize("x, y, expected", [(1, 2, 3), (-1, -2, -3), (0, 0, 0)])
    def test_add(self, x, y, expected):
        """Test the add method."""
        assert Calculator.add(x, y) == expected

    @pytest.mark.parametrize("x, y, expected", [(1, 2, -1), (-1, -2, 1), (0, 0, 0)])
    def test_subtract(self, x, y, expected):
        """Test the subtract method."""
        assert Calculator.subtract(x, y) == expected

    @pytest.mark.parametrize("x, y, expected", [(1, 2, 2), (-1, -2, 2), (0, 0, 0)])
    def test_multiply(self, x, y, expected):
        """Test the multiply method."""
        assert Calculator.multiply(x, y) == expected

    @pytest.mark.parametrize("x, y, expected", [(1, 2, 0.5), (-1, -2, 0.5), (1, 0, None)])
    def test_divide(self, x, y, expected):
        """Test the divide method."""
        if expected is None:
            with pytest.raises(ValueError):
                Calculator.divide(x, y)
        else:
            assert Calculator.divide(x, y) == expected
