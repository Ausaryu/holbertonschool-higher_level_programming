#!/usr/bin/python3
"""
This module contains a function that prints a text with proper indentation
after specific characters.
"""


def text_indentation(text):
    """
    Prints a text and adds two new lines after '.', '?' and ':' characters.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    newline = True
    for i in text:
        if newline is True:
            if i == ' ':
                continue
            else:
                newline = False
        print(f"{i}", end='')
        if i == '.' or i == '?' or i == ':':
            print('\n')
            newline = True
