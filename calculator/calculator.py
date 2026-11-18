"""A small calculator module used to demonstrate a basic CI pipeline.

The functions here are intentionally simple, but they cover the common
branches you want a test suite (and CI) to verify: normal results, edge
cases, and error handling.
"""

from __future__ import annotations


def add(a: float, b: float) -> float:
    """Return the sum of ``a`` and ``b``."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return ``a`` minus ``b``."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of ``a`` and ``b``."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return ``a`` divided by ``b``.

    Raises:
        ValueError: If ``b`` is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(a: float, b: float) -> float:
    """Return ``a`` raised to the power of ``b``."""
    return a**b


def main() -> None:
    """Print a few example calculations when run as a script."""
    print("CI Pipeline Basics - Calculator demo")
    print(f"add(2, 3)      = {add(2, 3)}")
    print(f"subtract(7, 4) = {subtract(7, 4)}")
    print(f"multiply(3, 5) = {multiply(3, 5)}")
    print(f"divide(10, 2)  = {divide(10, 2)}")
    print(f"power(2, 8)    = {power(2, 8)}")


if __name__ == "__main__":
    main()
