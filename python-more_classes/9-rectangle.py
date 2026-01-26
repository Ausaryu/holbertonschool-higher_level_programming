#!/usr/bin/python3
"""
This module defines a rectangle class used to represent a geometric Rectangle.
"""


class Rectangle:
    """
    This class represents a rectangle with a given size.
    """
    number_of_instances = 0
    print_symbol = '#'

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

        Rectangle.number_of_instances += 1
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        Returns a string representation of the rectangle using '#'.
        """
        result = ""
        for i in range(self.height):
            if i != self.height - 1:
                result += str(self.print_symbol) * self.width + '\n'
            else:
                result += str(self.print_symbol) * self.width
        return result

    def __repr__(self):
        """
        Returns a string representation of the rectangle for recreation.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        Rectangle.number_of_instances -= 1
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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
