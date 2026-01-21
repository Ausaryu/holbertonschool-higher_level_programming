#!/usr/bin/python3
"""
This module provides a function to add two numbers after validating their
types and converting them to integers if necessary.
"""


def add_integer(a, b=98):
    """
    Adds two numbers after checking that they are integers or floats and
    returns their sum as an integer.

    Args:
        a: The first number to add, must be an integer or a float.
        b: The second number to add, must be an integer or a float.

    Raises:
        TypeError: If a or b is not an integer or a float.

    Returns:
        The integer sum of a and b.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
