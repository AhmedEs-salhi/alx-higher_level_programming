#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str:
        return 0
    roman_numbers = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
    if len(roman_string) == 1:
        return roman_numbers[roman_string]
    integer_number = 0
    idx = 0
    while roman_string:
        print("index: {}".format(idx))
        if idx + 1 == len(roman_string):
            integer_number += roman_numbers[roman_string[idx]]
            break
        curr_ch = roman_string[idx]
        next_ch = roman_string[idx + 1]
        if roman_numbers[curr_ch] < roman_numbers[next_ch]:
            integer_number += roman_numbers[next_ch] - roman_numbers[curr_ch]
            idx += 2
            if idx == len(roman_string):
                break
        else:
            integer_number += roman_numbers[roman_string[idx]]
    return integer_number
