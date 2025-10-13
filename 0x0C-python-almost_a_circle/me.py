#!/usr/bin/python3

from models.rectangle import Rectangle
from models.square import Square

r1 = Rectangle(10, 7, 2, 8)
r2 = Rectangle(2, 4)
list_rectangles_input = [r1, r2]

Rectangle.save_to_file_csv(list_rectangles_input)

list_rectangles_output = Rectangle.load_from_file_csv()