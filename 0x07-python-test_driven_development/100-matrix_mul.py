#!/usr/bin/python3
"""This is the module docstring
"""


def is_list_of_lists(m):
    """Make sure wheter a matrix is a list of lists

    Args:
        m (list): The matrix to work on

    Returns:
        bool: True is the matrix is a list of lists.
        False otherwise
    """
    if type(m) is not list:
        return False, "must be a list"
    for i in m:
        if type(i) is not list:
            return False, "must be a list of lists"
    return True, ""


def matrix_mul(m_a, m_b):
    """Multiply two matrices by each other

    Args:
        m_a (list): The first matrix
        m_b (list): The second matrix

    Raises:
        TypeError: Raises in case of a matrix is not rectangle,
                   if a matrix does not contain only integers or floats,
                   if a matrix is not a list of lists,
                   if a matrix contains lists doesn't have the same size
        ValueError: Raises if both matrices can't be multiplied
                    or if a matrix is empty.

    Returns:
        list: The result of the multiplication
    """
    result, error_message = is_list_of_lists(m_a)
    if not result:
        raise TypeError("m_a {}".format(error_message))

    result, error_message = is_list_of_lists(m_b)
    if not result:
        raise TypeError("m_b {}".format(error_message))

    if m_a == [[]] or m_a == []:
        raise ValueError("m_a can't be empty")
    if m_b == [[]] or m_b == []:
        raise ValueError("m_b can't be empty")

    m_a_correct_rows_length = [len(m_a[0]) for i in range(len(m_a))]
    m_b_correct_rows_length = [len(m_b[0]) for i in range(len(m_b))]
    m_a_row_length = [len(m_a[i]) for i in range(len(m_a))]
    m_b_row_length = [len(m_b[i]) for i in range(len(m_b))]
    if m_a_correct_rows_length != m_a_row_length:
        raise TypeError("each row of m_a must be of the same size")
    if m_b_correct_rows_length != m_b_row_length:
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    c = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            result = 0
            for k in range(len(m_a[0])):
                if type(m_a[i][k]) not in [float, int]:
                    raise TypeError("m_a should contain only integers or \
floats")
                if type(m_b[k][j]) not in [float, int]:
                    raise TypeError("m_b should contain only integers or \
floats")
                result += m_a[i][k] * m_b[k][j]
            row.append(result)
        c.append(row)
    return c
