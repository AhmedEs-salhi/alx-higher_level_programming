#!/usr/bin/python3
string = "LXXXIVI"
roman_numbers = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
for i in range(len(string)):
    if i + 1 > len(string) - 1:
        print(i)
        exit(0)
    print("index: {}".format(i))
    if roman_numbers[string[i]] < roman_numbers[string[i + 1]]:
        print(i)
    print(roman_numbers[string[i]])
    if i > len(string) - 1:
        exit(0)
