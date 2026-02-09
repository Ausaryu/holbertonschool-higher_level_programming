#!/usr/bin/env python3
"""
This script demonstrates polymorphism by calling the sound method on
different animal objects.
"""

from task_00_abc import Animal, Dog, Cat

bobby = Dog()
garfield = Cat()

print(bobby.sound())
print(garfield.sound())

animal = Animal()
print(animal.sound())
