#!/usr/bin/python3
import sys

my_list = ["Ahmed", "Es-salhi"]
for i in range(1, len(sys.argv)):
    my_list.append(sys.argv[i])
print(my_list)