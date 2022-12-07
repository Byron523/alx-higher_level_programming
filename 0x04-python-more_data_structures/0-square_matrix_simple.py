#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = matrix.copy()

    for item in range(len(matrix)):
        new[item] = list(map(lambda x: x**2, matrix[item]))
    return (new)
