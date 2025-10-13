#!/usr/bin/python3
""" Check """
from models.square import Square

input_dict = { 'size': 2, 'name': "Ahmed", "age": 21}
keys = ['size', 'name', "age"]
values = [2, "Ahmed", 21]
new_dict = dict(zip(keys, values))


#for key, value in zip(keys, values):
#    new_dict[key] = value

print(new_dict, input_dict)
