#!/usr/bin/python3
def no_c(string):
    new_string = ""
    for i in range(len(string)):
        if string[i] == 'C' or string[i] == 'c':
            continue
        else:
            new_string += string[i]
    return new_string
