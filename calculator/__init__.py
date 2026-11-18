"""Calculator package for the CI Pipeline Basics demo.

Imports are lazy (PEP 562) so that running ``python -m calculator.calculator``
does not emit a "found in sys.modules" warning.
"""

from __future__ import annotations

from typing import Any

__all__ = ["add", "subtract", "multiply", "divide", "power", "calculate"]


def __getattr__(name: str) -> Any:
    if name in __all__:
        from . import calculator

        return getattr(calculator, name)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
