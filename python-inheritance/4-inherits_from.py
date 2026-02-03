#!/usr/bin/python3
"""
This module contains a function that checks if an object inherits from a
specified class but is not an instance of that class itself.
"""


def inherits_from(obj, a_class):
    """
    Checks if an object is an instance of a subclass of the given class.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
