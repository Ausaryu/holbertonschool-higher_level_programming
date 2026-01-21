#!/usr/bin/python3
"""
This module contains a function that divides all elements of a matrix by a
given number and returns a new matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides each element of a matrix by a number and returns a new matrix with
    the results rounded to two decimal places.
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    row_len = None

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists)/"
                            " of integers/floats")

        if row_len is None:
            row_len = len(row)
        elif len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")

        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of "
                                "integers/floats")

        new_matrix.append([round(i / div, 2) for i in row])

    return new_matrix
