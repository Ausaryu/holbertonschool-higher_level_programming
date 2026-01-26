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
        Initializes a Square instance with a given size.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """
        Returns the area of the square.
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        Retrieves the size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets a new size for the square.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
