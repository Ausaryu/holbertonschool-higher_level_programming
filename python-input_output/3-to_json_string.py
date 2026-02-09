#!/usr/bin/python3
"""
This module contains a function that converts a Python object into
a JSON string representation.
"""

from json import dumps


def to_json_string(my_obj):
    """
    Returns the JSON string representation of a Python object.
    """
    return dumps(my_obj)