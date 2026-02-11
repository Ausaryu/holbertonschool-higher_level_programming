#!/usr/bin/python3
"""
This module contains a function that saves a Python object to a JSON file.
"""

from json import dumps


def save_to_json_file(my_obj, filename):
    """
    Writes a Python object to a file using JSON representation.
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(dumps(my_obj))
