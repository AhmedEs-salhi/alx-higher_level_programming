#!/usr/bin/python3

def is_list_of_lists(m):
    if type(m) is not list:
        return False, "must be a list"
    for i in m:
        if type(i) is not list:
            return False, "must be a list of lists"
    return True, ""

def matrix_mul(m_a, m_b):
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
    
    c = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            if type(m_a[i][j]) not in [float, int]:
                raise TypeError("m_a should contain only integers or floats")
            if type(m_b[i][j]) not in [float, int]:
                raise TypeError("m_b should contain only integers or floats")
            result = 0
            for k in range(len(m_a[0])):
                result += m_a[i][k] * m_b[k][j]
            row.append(result)
        c.append(row)
    return c
