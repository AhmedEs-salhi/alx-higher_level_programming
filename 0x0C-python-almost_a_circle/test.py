#!/usr/bin/python3
""" Check """
from models.square import Square

input_dict = { 'size': 2 }
new_rect = Square.create(**input_dict)

print(new_rect.load_from_file())