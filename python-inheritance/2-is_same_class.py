#!/usr/bin/python3
"""
This module contains a function that checks if an object is exactly an
instance of a specified class.
"""


def is_same_class(obj, a_class):
    """
    Checks if an object is an instance of the given class.
    """
    return type(obj) is a_class
