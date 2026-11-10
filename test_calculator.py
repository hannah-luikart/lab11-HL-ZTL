import pytest
from calculator import add, subtract, multiply, divide, logarithm, exponent
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(3, 5) == -2
def test_divide_by_zero():
    with pytest.raises(Exception):
        divide(0, 5)
def test_logarithm():
    assert logarithm(2, 8) == 3.0


def test_log_invalid_base():
    with pytest.raises(Exception):
        logarithm(-2, 8)