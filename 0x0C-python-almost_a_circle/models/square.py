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

    @size.setter
    def size(self, size):
        self.width = size

    def update(self, *args, **kwargs):
        """ This is update method documentation """
        if args:
            attr_names = ['id', 'size', 'x', 'y']
            for i, value in enumerate(args):
                if i < len(attr_names):
                    setattr(self, attr_names[i], value)

        elif kwargs:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
                else:
                    mangledKey = "_{}__{}".format(self.__class__.__name__, key)
                    if hasattr(self, mangledKey):
                        setattr(self, mangledKey, value)

    def to_dictionary(self):
        """ This is to_dictionary method documentation """
        attr_names = ['x', 'y', 'id', 'size']
        a_dictionary = {}
        for index, key in enumerate(attr_names):
            mangled_key = "_{}__{}".format(self.__class__.__name__, key)
            if hasattr(self, mangled_key):
                a_dictionary[key] = getattr(self, mangled_key)
            else:
                a_dictionary[key] = getattr(self, key)
        return a_dictionary

    def __str__(self):
        """ This is __str__ method documentation """
        return "[{}] ({}) {}/{} - {}".format(
            self.__class__.__name__,
            self.id, self.x, self.y, self.width
        )
