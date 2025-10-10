#!/usr/bin/python3
""" This is method documentation """
from .rectangle import Rectangle


class Square(Rectangle):
    """ This is class documentation """
    def __init__(self, size, x=0, y=0, id=None):
        """ This is __init__ method documentation """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.getter
    def size(self, size):
        self.width = size

    def __str__(self):
        """ This is __str__ method documentation """
        return "[{}] ({}) {}/{} - {}".format(
            self.__class__.__name__,
            self.id, self.x, self.y, self.width
        )
