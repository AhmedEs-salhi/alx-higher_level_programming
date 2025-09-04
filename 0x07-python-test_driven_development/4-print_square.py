#!/usr/bin/python3
""" This is my module
"""


def print_square(size=None):
    """ Print a square of a certain size of '#'

    Args:
        size (int, optional): The size of the square. Defaults to None.

    Raises:
        TypeError: Raises When the size is not an int
        ValueError: Raises when the size is less than 0
    """
    if type(size) is not int or size is None\
            or size != size or size == float('inf'):
        raise TypeError("size must be an integer")
    if size < 0:
        if type(size) is float:
            raise TypeError("size must be an integer")
        raise ValueError("size must be >= 0")

    for row in range(size):
        for column in range(size):
            print("#", end="")
        print()
