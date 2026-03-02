#!/usr/bin/python3
"""
This module contains a function that generates Pascal's triangle.
"""


def pascal_triangle(n):
    """
    Returns a list of lists representing Pascal's triangle of size n.
    """
    triangle = []

    if n <= 0:
        return triangle
    for row in range(n):
        result = []
        if row == 0:
            result.append(1)
        else:
            for i in range(row + 1):
                if i == 0 or i == row:
                    result.append(1)
                else:
                    result.append(last_row[i] + last_row[i - 1])
        triangle.append(result)
        last_row = result
    return triangle
