#!/usr/bin/python3
""" This is module """

from .base import Base


class Rectangle(Base):
    """ This is the class documentation """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.y = y
