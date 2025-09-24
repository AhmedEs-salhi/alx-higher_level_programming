#!/usr/bin/python3
""" This is the module documentation
"""


class MyInt(int):
    """ This is the class documentation
    """
    def __init__(self, data):
        self._data = data

    def __eq__(self, data):
        return self._data != data

    def __ne__(self, data):
        return self._data == data
