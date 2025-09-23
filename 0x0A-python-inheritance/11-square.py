#!/usr/bin/python3
""" This is the module documentation
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ This is the class documentation
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        Rectangle.__init__(self, size, size)
        self._size = size

    def area(self):
        return self._size ** 2
