#!/usr/bin/python3
"""
This module defines a BaseGeometry class with basic geometric methods.
"""


class BaseGeometry:
    """
    This class provides a base for geometry-related operations.
    """

    def area(self):
        """
        Raises an exception indicating that the area method is not implemented.
        """
        raise Exception("area() is not implemented")