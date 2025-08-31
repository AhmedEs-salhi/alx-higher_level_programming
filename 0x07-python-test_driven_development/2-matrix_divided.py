#!/usr/bin/python3

""" Module description
"""


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
    length = len(matrix)
    rows_length = list(len(matrix[0]) * length for x in range(length))
    equal_rows_length = list(map(lambda x: len(x) * len(matrix), matrix))

    is_same_length = rows_length == equal_rows_length
    if type(matrix) is not list or matrix != matrix or \
            matrix == float('inf') or matrix == -float('inf'):
        raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
    if type(div) not in [int, float] or div != div or div == float('inf') \
            or div == -float('inf'):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not is_same_length:
        raise TypeError("Each row of the matrix must have the same size")

    new_matrix = []
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
        new_row = []
        for element in row:
            if type(element) not in [float, int] or element != element \
                    or element == float('inf') or element == -float('inf'):
                raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
            new_row.append(float("{0:.2f}".format(element / div)))
        new_matrix.append(new_row)
    return new_matrix
