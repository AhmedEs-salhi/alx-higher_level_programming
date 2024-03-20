#!/usr/bin/python3
def uppercase(string):
    for i in string :
        if ord(i) >= 97 and ord(i) <= 122:
            print("{}".format(chr(ord(i)-32)), end="")
        else:
            print("{}".format(i), end="")
