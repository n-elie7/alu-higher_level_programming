#!/usr/bin/python3
"""
This module provides a function that adds two integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats (after casting to integers).

    Args:
        a: The first number (int or float).
        b: The second number (int or float, default 98).

    Returns:
        int: The sum of a and b after converting to integers.

    Raises:
        TypeError: If a or b is not an int or float, or is NaN/inf.
    """
    for arg, name in ((a, "a"), (b, "b")):
        if not isinstance(arg, (int, float)):
            raise TypeError(f"{name} must be an integer")
        if isinstance(arg, float):
            if arg != arg or arg in (float("inf"), float("-inf")):
                raise TypeError(f"{name} must be an integer")

    return int(a) + int(b)
