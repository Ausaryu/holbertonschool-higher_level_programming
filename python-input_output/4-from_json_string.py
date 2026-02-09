#!/usr/bin/python3
"""
This module contains a function that converts a JSON string into
a corresponding Python object.
"""

from json import loads


def from_json_string(my_str):
    """
    Returns a Python object represented by a JSON string.
    """
    return loads(my_str)