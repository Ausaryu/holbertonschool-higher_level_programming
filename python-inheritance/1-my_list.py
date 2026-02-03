#!/usr/bin/python3
"""
This module defines a MyList class that extends the built-in list type.
"""


class MyList(list):
    """
    This class inherits from list and adds a method to print sorted elements.
    """

    def print_sorted(self):
        """
        Prints the list elements in ascending sorted order.
        """
        print(sorted(self))
