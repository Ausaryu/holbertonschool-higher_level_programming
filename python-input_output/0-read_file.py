#!/usr/bin/python3
"""
This module contains a function that reads a text file and prints its content.
"""


def read_file(filename=""):
    """
    Reads a text file and prints its content to standard output.
    """
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()

    print(read_data)
