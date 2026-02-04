#!/usr/bin/env python3
"""
This module defines mixin classes to add swimming and flying abilities
to other classes.
"""


class SwimMixin:
    """
    This mixin provides swimming behavior.
    """

    def swim(self):
        """
        Prints a message indicating that the creature can swim.
        """
        print("The creature swims!")


class FlyMixin:
    """
    This mixin provides flying behavior.
    """

    def fly(self):
        """
        Prints a message indicating that the creature can fly.
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    This class represents a dragon with swimming and flying abilities.
    """

    def roar(self):
        """
        Prints a message indicating that the dragon is roaring.
        """
        print("The dragon roars!")
