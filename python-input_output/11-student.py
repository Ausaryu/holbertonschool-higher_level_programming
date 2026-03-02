#!/usr/bin/python3
"""
This module defines a Student class used to represent a student and
serialize or update its attributes using JSON-compatible dictionaries.
"""


class Student:
    """
    This class represents a student with basic personal information.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance with first name, last name, and age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of the Student instance.

        If attrs is a list of strings, only attributes listed in attrs
        are included in the returned dictionary.
        """
        if isinstance(attrs, list) and all(isinstance(value, str)
                                           for value in attrs):
            result = {}
            for i in attrs:
                try:
                    result[i] = self.__dict__[i]
                except KeyError:
                    continue
            return result
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces the attributes of the Student instance using a dictionary.
        """
        for key, value in json.items():
            setattr(self, key, value)
