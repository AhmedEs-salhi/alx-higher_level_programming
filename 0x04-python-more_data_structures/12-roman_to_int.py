#!/usr/bin/python3
def roman_to_int(roman_string):
    number = 0
    a_dictionary = {"I":1, "V":5, "X":10, "L":50, "D":500, "M":1000,"C":100}
    if not roman_string:
        return 0
    for i in range(1, len(roman_string)):
        if roman_string[i] != roman_string[i - 1]:
            if roman_string[i - 1] < roman_string[i]:
                number += roman_string[i] - roman_string[i - 1]
            else:
                number += roman_string[i] + roman_string[i - 1]
    return number

roman_number = "X"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "VII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXXVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
