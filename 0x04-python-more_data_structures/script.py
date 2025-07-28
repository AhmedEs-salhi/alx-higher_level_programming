#!/usr/bin/python3
my_list = [(1, 2), (2, 1), (3, 10), (4, 2)]
temp_list = []
addition = 0
mult = 0
for i in my_list:
    temp_list = list(i)
    mult += temp_list[0] * temp_list[1]
    addition += temp_list[1]

print()
