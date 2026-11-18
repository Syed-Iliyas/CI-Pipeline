"""Tests for the calculator module.

Run locally with:

    pytest -q
"""

import pytest

from calculator import add, divide, multiply, power, subtract


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_subtract():
    assert subtract(7, 4) == 3
    assert subtract(4, 7) == -3


def test_multiply():
    assert multiply(3, 5) == 15
    assert multiply(-2, 4) == -8
    assert multiply(0, 99) == 0


def test_divide():
    assert divide(10, 2) == 5
    assert divide(7, 2) == 3.5


def test_divide_by_zero_raises():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)


def test_power():
    assert power(2, 8) == 256
    assert power(5, 0) == 1


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (1, 2, 3),
        (10, -5, 5),
        (2.5, 2.5, 5.0),
    ],
)
def test_add_parametrized(a, b, expected):
    assert add(a, b) == expected
