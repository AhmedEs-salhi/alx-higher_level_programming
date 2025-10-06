#!/usr/bin/python3
""" This is the module documentation """


def pascal_triangle(n):
    """ This is the function documentation"""

    pascal_triangle_list = [[1]]
    size = 2
    if n <= 0:
        return []
    if n == 1:
        return pascal_triangle_list

    previous_list = pascal_triangle_list[0]
    for i in range(1, n):
        list_to_add = [1]

        for j in range(1, size - 1):
            if len(previous_list) == 1:
                break

            list_to_add.append(previous_list[j - 1] + previous_list[j])

        list_to_add.append(1)
        pascal_triangle_list.append(list_to_add)
        previous_list = pascal_triangle_list[i]
        size += 1

    return pascal_triangle_list
