#!/usr/bin/python3
def remove_char_at(str, n):
    for i in str:
        if n >= 0 and i == str[n:n+1]:
            return str[:n] + str[n+1:]
