#!/usr/bin/python3
"""
This module defines a Square class used to represent a geometric square.
"""


class Square:
    """
    This class represents a square with a given size.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance with a specified size.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
