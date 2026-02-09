#!/usr/bin/python3
"""
This module defines a BaseGeometry class with basic geometric methods.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    This class represents a square using size.
    """

    def __init__(self, size):
        """
        Initializes a Square instance with validated size.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Returns the area of the square.
        """
        return super().area()
