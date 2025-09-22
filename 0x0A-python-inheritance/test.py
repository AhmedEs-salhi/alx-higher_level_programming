#!/usr/bin/env python3

def print_sorted(my_list):
    list_copy = my_list.copy()
    list_copy.sort()
    return list_copy

my_list = [3, 1, 5, 6]
print(print_sorted(my_list))
print(my_list)
