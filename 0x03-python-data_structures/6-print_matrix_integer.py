#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    if len(matrix) == 0:
        print("")
    for mat in matrix:
        if len(mat) == 0:
            print("")
        for i in range(len(mat)):
            print("{:d}".format(mat[i]), end="\n" if i is len(mat)-1 else " ")
