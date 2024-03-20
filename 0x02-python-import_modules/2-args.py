#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    length = len(argv) - 1
    if length == 1:
        print("{} argument.".format(length))
    elif length == 0:
        print("{} arguments.".format(length))
    else:
        print("{} arguments:".format(length))
    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
