#!/usr/bin/python3
"""
    Adding integer module
"""


def add_integer(a, b=98):
    """
        Adding integer function
        Args:
            a(int): The first integer
            b(int): The second optional integer
        Return:
            The sum of a and b
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
