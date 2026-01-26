#!/usr/bin/python3
"""
This module defines a rectangle class used to represent a geometric Rectangle.
"""


class Rectangle:
    """
    This class represents a rectangle with a given size.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance with a given height and height.
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

        self.__width = width
        self.__height = height

    def __str__(self):
        """
        Returns a string representation of the rectangle using '#'.
        """
        result = ""
        for i in range(self.height):
            if i != self.height - 1:
                result += '#' * self.width + '\n'
            else:
                result += '#' * self.width
        return result

    def __repr__(self):
        """
        Returns a string representation of the rectangle for recreation.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        return print("Bye rectangle...")

    @property
    def width(self):
        """
        Retrieves the width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets a new width for the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieves the height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets a new height for the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Returns the area of the rectangle.
        """
        return self.__height * self.width

    def perimeter(self):
        """
        Returns the perimeter of the rectangle.
        """
        return (self.__height * 2) + (self.width * 2)
