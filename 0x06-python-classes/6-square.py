#!/usr/bin/python3
""" This is the place where modules should be documented
"""


class Square:
    """ This is the documentation of our class

        Attributes:
            _Square__size (int): The size of the square object
    """
    def __init__(self, size=0, position=(0, 0)):
        """ This is the initilizer of the class object

            Args:
                size (int): The size of the square
            Raises:
                TypeError: If the size is not an integer
                ValueError: If the size is less than 0
        """
        self._Square__size = size
        self.__position = position

    @property
    def size(self):
        """ Getter method for assigning the value to the size attribute

            The setter method after this make sure that the size is an
            integer and bigger than 0, otherwise it will raise either
            a TypeError or a ValueError
        """
        return self._Square__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = value

    def area(self):
        """ Return the area of the current square object

            Returns:
                int: The area of the current square object created
        """
        return self._Square__size * self._Square__size

    @property
    def position(self):
        """ Getter method for assigning the value of the instance privat
            position attribute

            The setter method make sure that the position is of type tuple
            with two integer values, otherwise it will raise an TypeError
            with a particular message
        """
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """ Prints in stdout the square using the '#' symbol

            Returns: nothing, since it's just for writing on stdout
        """
        if self._Square__size == 0:
            print()
        for line in range(self.__position[1]):
            print()
        for line in range(self._Square__size):
            for colums in range(self.__position[0]):
                print(" ", end="")
            for columns in range(self._Square__size):
                print("#", end="")
            print('', end='\n')
