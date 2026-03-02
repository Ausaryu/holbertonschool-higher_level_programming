#!/usr/bin/python3
"""
This module defines a Student class used to represent a student and
convert its attributes into a dictionary.
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

    def to_json(self):
        """
        Returns a dictionary representation of the Student instance.
        """
        return self.__dict__
