#!/usr/bin/python3
""" This is module documentation """

from .base import Base


class Rectangle(Base):
    """ This is the class documentation """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ This is __init__ function documentation"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ This is width getter documentation"""
        return self.__width

    @width.setter
    def width(self, width):
        """ This is width setter documentation """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """ This is height getter documentation """
        return self.__height

    @height.setter
    def height(self, height):
        """ This is height setter documentation """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """ This is x getter function documentation"""
        return self.__x

    @x.setter
    def x(self, x):
        """ This is x setter documentation """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """ This is y getter function documentation """
        return self.__y

    @y.setter
    def y(self, y):
        """ This is y setter function documentation """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """ This is area method documentation """
        return self.height * self.width

    def display(self):
        """ This is display method documentation """
        output = "\n" * self.y
        for i in range(self.height):
            output += " " * self.x + "#" * self.width + "\n"
        print(output[:-1])

    def __str__(self):
        """ This is __str__ method documentation """
        return "[{}] ({}) {}/{} - {}/{}".format(
            self.__class__.__name__,
            self.id, self.x, self.y, self.width, self.height
        )

    def update(self, *args, **kwargs):
        """ This is update method documentation """
        #print("kwargs len: {}".format(len(kwargs)))
        #print("args len: {}".format(len(args)))

        attributes_dict = self.__dict__
        if len(args) == 0:
            for key in kwargs:
                for attr_dict_key in attributes_dict:
                    if key == attr_dict_key[12:] or key == attr_dict_key:
                        attributes_dict[attr_dict_key] = kwargs[key]
                    else:
                        continue
        else:
            attributes_dict["id"] = args[0]
            index = 1
            for key in attributes_dict:
                if key == "id":
                    continue
                try:
                    attributes_dict[key] = args[index]
                except IndexError:
                    break
                else:
                    index += 1
        #print(attributes_dict)
