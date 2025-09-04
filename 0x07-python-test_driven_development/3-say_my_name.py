#!/usr/bin/python3
"""
This is my module
"""


def say_my_name(first_name, last_name=""):
    """
    Function that print a salutation text with both arguments

    Args:
        first_name (string): user's first name
        last_name (string): user's last name
    Raises:
        TypeError: When one or both of strings are not an actual string
    Returns:
        Nothing
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
