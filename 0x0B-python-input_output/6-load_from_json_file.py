#!/usr/bin/python3
""" This is the module documentation """
import json


def load_from_json_file(filename):
    """ This is the function documentation """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
