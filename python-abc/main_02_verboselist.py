#!/usr/bin/env python3
"""
This script demonstrates the behavior of the VerboseList class by performing
several list operations and displaying their effects.
"""

from task_02_verboselist import VerboseList

vl = VerboseList([1, 2, 3])
vl.append(4)
vl.extend([5, 6])
vl.remove(2)
vl.pop()
vl.pop(0)
