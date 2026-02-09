#!/usr/bin/python3
"""
This module contains a function that returns a dictionary representation
of an object suitable for JSON serialization.
"""

from json import dumps


def class_to_json(obj):
    """
    Returns the dictionary description of an object.
    """
    return obj.__dict__