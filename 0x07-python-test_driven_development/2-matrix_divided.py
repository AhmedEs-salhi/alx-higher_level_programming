#!/usr/bin/python3

""" Module description
"""


def is_same_length(my_list):
    """ Function that assure wheter a matrix (list of lists)
        have rows with the same size.

    Args:
        my_list (list): The matrix to work on.

    Returns:
        bool: True if the matrix have rows with the same size.
        False otherwize.
    """
    length = my_list[0]
    for idx in range(1, len(my_list)):
        if my_list[idx] != length:
            return False
    return True


def matrix_divided(matrix, div):

    """ Function that divided every single
        element of a matrix by the argument div

    Args:
        matrix (list): list of lists of integers/floats
        div (int/float): matrix element divisor

    Raises:
        TypeError: raises when the matrix is not a list of lists
            of integers/floats
            or its rows have not the same size
        ZeroDivisionError: raises when we divide by 0

    Returns:
        list: a matrix list of lists of floats where
        evey element is divided by div
    """
    if type(matrix) is not list or matrix != matrix or \
            matrix == float('inf') or matrix == -float('inf'):
        raise TypeError("matrix must be a matrix (list of lists) \
            of integers/floats")
    if type(div) not in [int, float] or div != div or div == float('inf') \
            or div == -float('inf'):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not is_same_length(list(map(lambda x: len(x), matrix))):
        raise TypeError("Each row of the matrix must have the same size")

    new_matrix = []
    for row in matrix:
        if type(row) is list:
            raise TypeError("matrix must be a matrix (list of lists) of \
                integers/floats")
        new_row = []
        for element in row:
            if type(element) not in [float, int] or element != element \
                    or element == float('inf') or element == -float('inf'):
                raise TypeError("matrix must be a matrix (list of lists)\
                    of integers/floats")
            new_row.append(float("{0:.2f}".format(element / div)))
        new_matrix.append(new_row)
    return new_matrix
