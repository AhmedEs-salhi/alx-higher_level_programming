#!/usr/bin/python3
""" This is the module documentation
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ This is the class documentation
    """
    def __init__(self, width, height):
        self.integer_validator("height", height)
        self.integer_validator("width", width)
        self._width = width
        self._height = height

    def area(self):
        return self._height * self._width

    def __str__(self):
        return "[{}] {}/{}".format(self.__class__.__name__,
                                   self._width,
                                   self._height)
