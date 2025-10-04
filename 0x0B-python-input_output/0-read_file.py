#!/usr/bin/pyton3
""" This is the module documentation """


def read_file(filename=""):
    """ This is the function documentation """

    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
