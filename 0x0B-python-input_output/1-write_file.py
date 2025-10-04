#!/usr/bin/python3
""" This is the module documentation"""


def write_file(filename="", text=""):
    """ This is the function documentation """

    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
