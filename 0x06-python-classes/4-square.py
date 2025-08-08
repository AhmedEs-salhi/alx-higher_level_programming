#!/usr/bin/python3
import dis
""" This is the place where modules should be documented
"""


class Square:
    """ This is the documentation of our class

        Attributes:
            _Square__size (int): The size of the square object
    """
    def __init__(self, size=0):
        """ This is the initilizer of the class object

            Args:
                size (int): The size of the square
            Raises:
                TypeError: If the size is not an integer
                ValueError: If the size is less than 0
        """
        self._Square__size = size

    @property
    def size(self):
        return self._Square__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise TypeError("size must be >= 0")
        self._Square__size = value

    def area(self):
        """ Return the area of the current square object

            Returns:
                int: The area of the current square object created
        """
        return self._Square__size * self._Square__size
dis.dis(Square)
