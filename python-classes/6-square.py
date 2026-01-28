#!/usr/bin/python3
"""
This module defines a Square class used to represent a geometric square.
"""


class Square:
    """
    This class represents a square with a given size.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square instance with a given size.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if (
            not isinstance(position, tuple)
            or len(position) != 2
            or not type(position[0]) is int
            or not type(position[1]) is int
            or position[0] < 0 or position[1] < 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """
        Retrieves the position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets a new position for the square.
        """
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not type(value[0]) is int
            or not type(value[1]) is int
            or value[0] < 0 or value[1] < 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """
        Prints the square using the '#' character.
        """
        size = self.__size
        position = self.__position

        for i in range(position[1]):
            print()
        if size == 0:
            print()
        else:
            for i in range(size):
                print(position[0] * ' ' + '#' * size)
