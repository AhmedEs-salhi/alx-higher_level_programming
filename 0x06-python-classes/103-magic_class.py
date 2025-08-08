#!/usr/bin/python3
import math
""" Math module for some mathematical calculation.

    Raises:
        TypeError: In case the radius given is neither an integer
        nor a float.
"""


class MagicClass:
    """ Class for translating the python bytecode

        Attributes:
            _MagicClass_radius: integer/float number containing the radius
    """
    def __init__(self, radius):
        """ The Attribute initilizer

        Args:
            radius (int): Represent the radius given by the user

        Raises:
            TypeError: in case of the radius variable is neither an int
            nor a float
        """
        self._MagicClass_radius = 0
        if type(radius) is not int:
            if type(radius) is not float:
                raise TypeError("radius must be a number")
        self._MagicClass_radius = radius

    def area(self):
        """ Return the area of the circle based on its radius

        Returns:
            float: the area of the circle
        """
        return self._MagicClass_radius ** 2 * math.pi

    def circumference(self):
        """ Return the boundries length of a circle

        Returns:
            float: The circumference calculated
        """
        return 2 * math.pi * self._MagicClass_radius
