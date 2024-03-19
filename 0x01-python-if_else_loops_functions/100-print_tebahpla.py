#!/usr/bin/python3
for i in range(ord('z'), ord('a')-1, -1):
        print(f"{chr(i)}", end="")
        print(f"{chr(ord(chr(i+1-32)))}", end="")

