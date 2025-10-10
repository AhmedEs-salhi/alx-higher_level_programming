#!/usr/bin/python3
""" This is method documentation """
from .rectangle import Rectangle


class Square(Rectangle):
    """ This is class documentation """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[{}] ({}) {}/{} - {}".format(
            self.__class__.__name__,
            self.width, self.x, self.y, self.id
        )