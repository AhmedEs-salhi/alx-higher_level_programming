#!/usr/bin/python3
""" This is the module documentation """
import json
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file


def class_to_json(obj):
    """ This is the function documentation """
    return json.dumps(obj.__dict__)
