#!/usr/bin/python3
import sys
length = len(sys.argv) - 1
if __name__ == "__main__":
    if length == 1:
        print("{} argument.".format(length))
    elif length == 0:
        print("{} arguments.".format(length))
    else:
        print("{} arguments:".format(length))
    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))
