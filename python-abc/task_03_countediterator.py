#!/usr/bin/env python3
"""
This module defines a CountedIterator class that wraps an iterable and
counts how many elements have been iterated over.
"""


class CountedIterator:
    """
    This class implements an iterator that counts each retrieved element.
    """

    def __init__(self, object):
        """
        Initializes the iterator with an iterable object.
        """
        self.__iter = iter(object)
        self.__count = 0

    def get_count(self):
        """
        Returns the number of elements that have been iterated.
        """
        return self.__count

    def __next__(self):
        """
        Returns the next element from the iterator and increments the counter.
        """
        value = next(self.__iter)
        self.__count += 1
        return value
