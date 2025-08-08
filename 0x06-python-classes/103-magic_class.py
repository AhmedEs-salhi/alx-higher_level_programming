#!/usr/bin/python3
import math
""" Importing math module for using pi number in the mathematical calculatin
"""


class MagicClass:
    """ Class documentation
        Containing several methods based on mathematical calculation
        just to test the their bytecode
    """
    def __init__(self, radius):
        self._MagicClass_radius = 0
        if type(radius) is not int:
            if type(radius) is not float:
                raise TypeError("radius must be a number")
        self._MagicClass_radius = radius

    def area(self):
        return self._MagicClass_radius ** 2 * math.pi

    def circumference(self):
        return 2 * math.pi * self._MagicClass_radius
