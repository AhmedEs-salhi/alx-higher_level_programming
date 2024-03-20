#!/usr/bin/python3
for i in range(ord('z'), ord('a')-1, -1):
    j = i
    if i % 2 == 1:
        j = i - 32
    print("{}".format(chr(j)), end="")
