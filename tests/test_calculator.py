"""Tests for the calculator module.

Run locally with:

    pytest -q
"""

import pytest

from calculator import add, calculate, divide, multiply, power, subtract
from calculator.calculator import main, run_interactive


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


@pytest.mark.parametrize(
    "operation,a,b,expected",
    [
        ("add", 2, 3, 5),
        ("subtract", 7, 4, 3),
        ("multiply", 3, 5, 15),
        ("divide", 10, 2, 5),
        ("power", 2, 8, 256),
        ("ADD", 2, 3, 5),  # operation names are case-insensitive
    ],
)
def test_calculate_dispatch(operation, a, b, expected):
    assert calculate(operation, a, b) == expected


def test_calculate_unknown_operation():
    with pytest.raises(ValueError, match="Unknown operation"):
        calculate("modulo", 10, 3)


def test_main_with_arguments(capsys):
    main(["add", "2", "3"])
    assert "Result: 5" in capsys.readouterr().out


def test_main_rejects_divide_by_zero(capsys):
    with pytest.raises(SystemExit):
        main(["divide", "10", "0"])
    assert "Cannot divide by zero" in capsys.readouterr().err


def test_main_interactive_exits(monkeypatch, capsys):
    answers = iter(["quit"])
    monkeypatch.setattr("builtins.input", lambda _: next(answers))
    run_interactive()
    output = capsys.readouterr().out
    assert "Interactive calculator" in output
    assert "Goodbye!" in output


def test_main_interactive_calculation(monkeypatch, capsys):
    answers = iter(["add", "2", "3", "quit"])
    monkeypatch.setattr("builtins.input", lambda _: next(answers))
    run_interactive()
    output = capsys.readouterr().out
    assert "Result: 5" in output
    assert "Goodbye!" in output


def test_main_interactive_eof(monkeypatch, capsys):
    def raise_eof(_):
        raise EOFError

    monkeypatch.setattr("builtins.input", raise_eof)
    run_interactive()
    assert "Goodbye!" in capsys.readouterr().out
