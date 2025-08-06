#!/usr/bin/python3
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
        if type(size) is not int:
            raise TypeError("Size must be an integer")
        if size < 0:
            raise TypeError("Size must be >= 0")
        self._Square__size = size
