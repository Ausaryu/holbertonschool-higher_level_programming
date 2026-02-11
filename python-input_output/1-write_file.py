#!/usr/bin/python3
"""
This module contains a function that writes text to a file.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file and returns the number of characters.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
