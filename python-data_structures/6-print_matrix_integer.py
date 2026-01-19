#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print()
        return
    for i in matrix:
        for y in range(len(i)):
            if y != len(i) - 1:
                print("{}".format(i[y]), end=" ")
            else:
                print("{}".format(i[y]))
