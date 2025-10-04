#!/usr/bin/python3
""" This is the module documentation """
import json


def save_to_json_file(my_obj, filename):
    """ This is the function documentation """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
