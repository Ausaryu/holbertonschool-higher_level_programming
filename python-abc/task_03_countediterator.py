#!/usr/bin/env python3

class CountedIterator():
    def __init__(self, object):
        self.__iter = iter(object)
        self.__count = 0

    def get_count(self):
        return self.__count

    def __next__(self):
        value = next(self.__iter)
        self.__count += 1
        return value
