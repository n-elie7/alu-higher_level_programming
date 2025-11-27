#!/usr/bin/python3
"""
Module for adding two integers.
This module contains a function that adds two numbers after
casting them to integers if they are floats.
"""


def add_integer(a, b=98):
    """
    Adds two integers.
    Args:
        a: First number (int or float)
        b: Second number (int or float), defaults to 98
    Returns:
        The addition of a and b as an integer
    Raises:
        TypeError: If a or b is not an integer or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Check for NaN and infinity
    if a != a or a == float("inf") or a == float("-inf"):
        raise TypeError("a must be an integer")
    if b != b or b == float("inf") or b == float("-inf"):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
