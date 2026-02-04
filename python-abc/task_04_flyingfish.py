#!/usr/bin/env python3
"""
This module defines classes to demonstrate multiple inheritance using
fish and bird behaviors.
"""


class Fish:
    """
    This class represents a fish.
    """

    def swim(self):
        """
        Prints a message indicating that the fish is swimming.
        """
        print("The fish is swimming")

    def habitat(self):
        """
        Prints the natural habitat of the fish.
        """
        print("The fish lives in water")


class Bird:
    """
    This class represents a bird.
    """

    def fly(self):
        """
        Prints a message indicating that the bird is flying.
        """
        print("The bird is flying")

    def habitat(self):
        """
        Prints the natural habitat of the bird.
        """
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    This class represents a flying fish using multiple inheritance.
    """

    def fly(self):
        """
        Prints a message indicating that the flying fish is flying.
        """
        print("The flying fish is soaring!")

    def swim(self):
        """
        Prints a message indicating that the flying fish is swimming.
        """
        print("The flying fish is swimming!")

    def habitat(self):
        """
        Prints the habitat of the flying fish.
        """
        print("The flying fish lives both in water and the sky!")
