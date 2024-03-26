#!/usr/bin/python3
def complex_delete(a_dictionary, key=""):
    for i in a_dictionary:
        if key in a_dictionary:
            del a_dictionary[key]
    return a_dictionary
