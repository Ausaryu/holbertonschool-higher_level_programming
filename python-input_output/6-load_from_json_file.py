#!/usr/bin/python3
"""
This module contains a function that loads a Python object from a JSON file.
"""

from json import loads


def load_from_json_file(filename):
    """
    Reads a JSON file and returns the corresponding Python object.
    """
    with open(filename, encoding="utf-8") as f:
        return loads(f.read())
