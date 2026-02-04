#!/usr/bin/env python3
"""
This module defines an abstract Animal class and concrete subclasses
that implement specific animal sounds.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    This abstract class represents an animal.
    """

    @abstractmethod
    def sound(self):
        """
        Returns the sound made by the animal.
        """
        pass


class Dog(Animal):
    """
    This class represents a dog.
    """

    def sound(self):
        """
        Returns the sound made by the dog.
        """
        return "Bark"


class Cat(Animal):
    """
    This class represents a cat.
    """

    def sound(self):
        """
        Returns the sound made by the cat.
        """
        return "Meow"
