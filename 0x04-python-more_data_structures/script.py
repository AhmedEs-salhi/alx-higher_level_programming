#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0
    roman_numbers = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
    if len(roman_string) == 1:
        return roman_numbers[roman_string]
    integer_number = 0
    for idx in range(len(roman_string)):
        if idx + 1 == len(roman_string):
            integer_number += roman_numbers[roman_string[idx]]
            break
        if roman_numbers[roman_string[idx]] < roman_numbers[roman_string[idx + 1]]:
            integer_number += roman_numbers[roman_string[idx + 1]] - roman_numbers[roman_string[idx]]
            idx += 2
            if idx == len(roman_string):
                break
        else:
            integer_number += roman_numbers[roman_string[idx]]
    return integer_number

roman_number = 'X'
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "VII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LIV"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXXVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
