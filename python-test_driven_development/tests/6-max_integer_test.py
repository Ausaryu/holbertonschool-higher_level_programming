#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        with self.assertRaises(TypeError):
            max_integer([1, 2, "a", 4])

        self.assertEqual(max_integer(), None)

        self.assertEqual(max_integer([-4, -6, -9]), -4)

        with self.assertRaises(TypeError):
            max_integer([1, 3, 4, 2], [1, 3, 4, 2])

        self.assertEqual(max_integer("aaaaabc"), 'c')

        self.assertEqual(max_integer([1, 7.9, 3.7, 4, 2]), 7.9)

        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

        self.assertEqual(max_integer([1, 3, 4, float('inf'), 2]), float('inf'))
