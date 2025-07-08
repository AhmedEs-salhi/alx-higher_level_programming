#!/usr/bin/python3
def remove_char_at(string, index):
    other_string = ""
    for i in range(len(string)):
        if i == index:
            continue
        other_string += string[i]
    return other_string
