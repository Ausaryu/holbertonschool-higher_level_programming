#!/usr/bin/env python3
"""
This module defines a VerboseList class that extends the built-in list
and prints messages when the list is modified.
"""


class VerboseList(list):
    """
    This class extends the list type by displaying messages for each operation.
    """

    def append(self, item):
        """
        Adds an item to the list and prints a confirmation message.
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, item):
        """
        Extends the list with multiple items and prints a summary message.
        """
        len_item = len(item)
        super().extend(item)
        print(f"Extended the list with [{len_item}] items.")

    def remove(self, item):
        """
        Removes an item from the list and prints a confirmation message.
        """
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """
        Removes and returns an item from the list and prints a message.
        """
        print(f"Popped [{self[index]}] from the list.")
        return super().pop(index)
