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
            raise TypeError("size must be an integer")
        if size < 0:
            raise TypeError("size must be >= 0")
        self._Square__size = size

    def area(self):
        """ Return the area of the current square object

            Returns:
                int: The area of the current square object created
        """
        return self._Square__size * self._Square__size
