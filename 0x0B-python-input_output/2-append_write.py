#!/usr/bin/python3
""" This is the module documentation"""


def append_write(filename="", text=""):
    """ This is the function documentation """

    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
