#!/usr/bin/env python3
"""
This module defines abstract and concrete shape classes and provides a
function to display shape information.
"""

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """
    This abstract class defines the interface for geometric shapes.
    """

    @abstractmethod
    def area(self):
        """
        Returns the area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Returns the perimeter of the shape.
        """
        pass


class Circle(Shape):
    """
    This class represents a circle defined by its radius.
    """

    def __init__(self, radius):
        """
        Initializes a Circle instance with a given radius.
        """
        self.__radius = radius

    def area(self):
        """
        Returns the area of the circle.
        """
        return pi * self.__radius ** 2

    def perimeter(self):
        """
        Returns the perimeter of the circle.
        """
        return 2 * pi * abs(self.__radius)


class Rectangle(Shape):
    """
    This class represents a rectangle defined by width and height.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with given width and height.
        """
        self.__width = width
        self.__height = height

    def area(self):
        """
        Returns the area of the rectangle.
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Returns the perimeter of the rectangle.
        """
        return (self.__height * 2) + (self.__width * 2)


def shape_info(shape):
    """
    Prints the area and perimeter of a given shape.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
