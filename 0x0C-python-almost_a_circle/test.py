#!/usr/bin/python3
import json
list_dict_json = []
a_dictionary = {"name": "Ahmed", "age": 21, "CNE": 2229307}
list_dict_json.append(a_dictionary)
list_dict_json = json.dumps(list_dict_json)
print(list_dict_json, type(list_dict_json))


def func(number):
    if number:
        return number
    return "It's None you idiot"

print(func(1024))
print(func(None))
