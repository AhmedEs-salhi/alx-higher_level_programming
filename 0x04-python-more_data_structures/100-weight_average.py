#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    up = 0
    down = 0
    for tuple_element in my_list:
        tuple_list = list(tuple_element)
        up += tuple_list[0] * tuple_list[1]
        down += tuple_list[1]
    return float(up / down)
