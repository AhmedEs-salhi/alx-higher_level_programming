#!/usr/bin/python3
"""
    Adding integer module
"""


def add_integer(a, b=98):
    """
        Adding integer function
        Args:
            a(int): The first integer
            b(int, optional): The second optional integer. Defaults to 98
        Return:
            The sum of a and b
    """
    if type(a) not in [int, float] or a != a or a == float('inf')\
            or a == -float('inf'):
        raise TypeError("a must be an integer")
    if type(b) not in [int, float] or b != b or b == float('inf')\
            or b == -float('inf'):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
