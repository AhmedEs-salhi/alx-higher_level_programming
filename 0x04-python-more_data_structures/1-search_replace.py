#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    return list(map(lambda x: replace if x == search else x, my_list))
