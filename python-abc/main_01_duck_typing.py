#!/usr/bin/env python3
"""
This script demonstrates duck typing by calling a function that works
with different shape objects sharing the same behavior.
"""

from task_01_duck_typing import Circle, Rectangle, shape_info

circle = Circle(radius=5)
rectangle = Rectangle(width=4, height=7)

shape_info(circle)
shape_info(rectangle)
