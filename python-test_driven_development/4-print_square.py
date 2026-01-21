#!/usr/bin/python3
"""
This module contains a function that prints a square using the character '#'.
"""


def print_square(size):
    """
    Prints a square of size `size` using the '#' character.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if 0 > size:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print('#' * size)
