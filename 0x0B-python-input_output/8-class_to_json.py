#!/usr/bin/python3
""" This is the module documentation """

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file


def class_to_json(obj):
    """ This is the function documentation """
    save_to_json_file(obj.__dict__, "class.json")
    with open("class.json", "r", encoding="utf-8") as file:
        return file.read()

