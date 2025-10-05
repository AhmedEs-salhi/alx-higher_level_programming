#!/usr/bin/python3
""" This is the module documentation """
import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


def add_item(obj):
    """ This is the function documentation """
    temp_obj = []
    for i in range(1, len(sys.argv)):
        temp_obj.append(sys.argv[i])
    try:
        obj = load_from_json_file("add_item.json")
    except Exception:
        if len(sys.argv) != 0:
            obj += temp_obj
        save_to_json_file(obj, "add_item.json")
    else:
        obj += temp_obj
        save_to_json_file(obj, "add_item.json")


add_item([])
