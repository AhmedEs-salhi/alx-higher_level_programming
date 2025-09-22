#!/usr/bin/python3
""" This is the module documentation
"""


class MyList(list):
    """ This is the method documentation
    """
    def print_sorted(self):
        list_copy = self.copy()
        list_copy.sort()
        print(list_copy)
