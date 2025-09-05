#!/usr/bin/python3
"""
This is my module
"""


def say_my_name(first_name=None, last_name=""):
    """
    Function that print a salutation text with both arguments

    Args:
        first_name (string, optional): user's first name. Defaults to None
        last_name (string, optional): user's last name. Defaults to ""
    Raises:
        TypeError: When one or both of strings are not an actual string
    Returns:
        Nothing
    """
    if type(first_name) is not str or first_name is None:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str or last_name is None:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
