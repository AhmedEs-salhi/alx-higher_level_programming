#!/usr/bin/python3
""" This is the module documentation """
import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


def add_item(obj=[]):
    """ This is the function documentation """
    if len(sys.argv) == 0:
        obj = []
    try:
        obj = load_from_json_file("add_item.json")
    except Exception:
        with open("add_item.json", "w", encoding="utf-8") as file:
            file.write("[]")
        obj = []
    else:
        for i in range(1, len(sys.argv)):
            obj.append(sys.argv[i])
    finally:
        save_to_json_file(obj, "add_item.json")

add_item([])
