"""A small calculator module used to demonstrate a basic CI pipeline.

The functions here are intentionally simple, but they cover the common
branches you want a test suite (and CI) to verify: normal results, edge
cases, and error handling. The module can be used three ways:

1. Import the functions in your own Python code.
2. Pass arguments on the command line, e.g.
   ``python -m calculator.calculator add 2 3``.
3. Run with no arguments for an interactive prompt.
"""

from __future__ import annotations

import argparse

OPERATIONS = {
    "add": "Addition",
    "subtract": "Subtraction",
    "multiply": "Multiplication",
    "divide": "Division",
    "power": "Exponentiation",
}


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


_FUNCTIONS = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide,
    "power": power,
}


def calculate(operation: str, a: float, b: float) -> float:
    """Call the function named by ``operation`` with ``a`` and ``b``.

    Raises:
        ValueError: If the operation is unknown or the arguments are invalid
            (for example, dividing by zero).
    """
    try:
        function = _FUNCTIONS[operation.lower()]
    except KeyError as exc:
        raise ValueError(f"Unknown operation: {operation}") from exc
    return function(a, b)


def _prompt(message: str) -> str | None:
    """Read a line of input, returning None on EOF or Ctrl+C."""
    try:
        return input(message)
    except (EOFError, KeyboardInterrupt):
        print()
        return None


def _read_number(prompt: str) -> float | None:
    """Prompt until the user enters a valid number, or None if input ends."""
    while True:
        value = _prompt(prompt)
        if value is None:
            return None
        try:
            return float(value.strip())
        except ValueError:
            print("Please enter a valid number.")


def run_interactive() -> None:
    """Run a loop that asks the user for an operation and two numbers."""
    choices = ", ".join(OPERATIONS)
    print(f"Interactive calculator. Available operations: {choices}.")
    print("Type 'quit' (or 'q' / 'exit') to stop.\n")

    while True:
        answer = _prompt(f"Operation [{choices}]: ")
        if answer is None:
            print("Goodbye!")
            break
        operation = answer.strip().lower()
        if operation in {"quit", "q", "exit"}:
            print("Goodbye!")
            break
        if operation not in OPERATIONS:
            print(f"Unknown operation. Choose from: {choices}.\n")
            continue

        a = _read_number("First number:  ")
        if a is None:
            print("Goodbye!")
            break
        b = _read_number("Second number: ")
        if b is None:
            print("Goodbye!")
            break
        try:
            result = calculate(operation, a, b)
        except ValueError as exc:
            print(f"Error: {exc}\n")
        else:
            print(f"Result: {result}\n")


def main(argv: list[str] | None = None) -> None:
    """Entry point for ``python -m calculator.calculator``.

    With no arguments, starts interactive mode. When an operation is given,
    both numbers must be supplied as positional arguments.
    """
    parser = argparse.ArgumentParser(
        description="A small calculator. Run with no arguments for interactive mode."
    )
    parser.add_argument(
        "operation",
        nargs="?",
        type=str.lower,
        choices=list(OPERATIONS),
        help="the operation to perform",
    )
    parser.add_argument("a", nargs="?", type=float, help="the first number")
    parser.add_argument("b", nargs="?", type=float, help="the second number")
    args = parser.parse_args(argv)

    if args.operation is None:
        run_interactive()
        return

    if args.a is None or args.b is None:
        parser.error("both numbers are required when an operation is given")

    try:
        result = calculate(args.operation, args.a, args.b)
    except ValueError as exc:
        parser.error(str(exc))
    print(f"Result: {result}")


if __name__ == "__main__":
    main()
