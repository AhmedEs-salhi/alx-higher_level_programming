#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for i in a_dictionary:
        if value not in a_dictionary:
            return a_dictionary
        if a_dictionary[i] == value:
            del a_dictionary[i]
    return a_dictionary
