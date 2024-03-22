#!/usr/bin/python3
def no_c(my_string):
    for i in range(0, len(my_string)):
        if my_string[i] == 'C' or my_string[i] == 'c':
            my_string.remove(my_string[i])
    return my_string
