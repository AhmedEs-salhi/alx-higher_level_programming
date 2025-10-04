#!/usr/bin/python3
""" Module documentation """


def add_attribute(obj, attr, value):
    """ Function Documentation
    """

    if type(obj) in [int, str, tuple, list, dict, bool, None]:
        raise TypeError("can't add new attribute")
    obj.__setattr__(str(attr), str(value))
