#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix == []:
        return
    new_matrix = matrix.copy()
    for x in range(len(matrix)):
        new_matrix[x] = matrix[x].copy()
        for i in range(len(new_matrix[x])):
            new_matrix[x][i] = new_matrix[x][i] ** 2
    return new_matrix
