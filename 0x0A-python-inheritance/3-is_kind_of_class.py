#!/usr/bin/python3
""" This is the module documentation
"""


def is_kind_of_class(obj, a_class):
    """ The function documentation
    """
    return isinstance(obj, a_class) or issubclass(obj.__class__, a_class)
