#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
        if len(matrix) <= 0:
                print('$')
        else:
                for i in matrix:
                        for j in range(len(matrix)):
                                print("{} ".format(i[j]), end='')
                        print('$')
