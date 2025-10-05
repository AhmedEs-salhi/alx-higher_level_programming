#!/usr/bin/python3

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
import sys
import json

def add_item(obj):
    temp_obj = []
    for i in range(1, len(sys.argv)):
        temp_obj.append(sys.argv[i])
    try:
        obj = load_from_json_file("add_item.json")
    except Exception:

        # Means that the file doesn't exist yet
        # So I have to Create the file and either:
            # Put "[]" inside (There is no arguments)
            # Or the full list with argument appended (There is arguments)

        if len(sys.argv) != 0:
            obj += temp_obj
        save_to_json_file(obj, "add_item.json")
    else:
        obj += temp_obj
        save_to_json_file(obj, "add_item.json")

add_item(["First"])