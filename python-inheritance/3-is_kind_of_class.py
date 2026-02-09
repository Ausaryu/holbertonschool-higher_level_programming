#!/usr/bin/python3
"""
This module contains a function that checks if an object is an instance of
a given class or of a class that inherits from it.
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of the given class or its subclasses.
    """
    return isinstance(obj, a_class)
