#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    length = len(sys.argv)
    somme = 0
    for i in range(1, length):
        somme += int(sys.argv[i])
    print(somme)
