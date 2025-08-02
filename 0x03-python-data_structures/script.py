#!/usr/bin/python3
import sys

def compare_strings(string_1, string_2):
    """ Compare Two strings
        Return True if both strings are identical
        False otherwise.
    """
    if string_1 == string_2:
        return True
    return False

print(compare_strings.__doc__)
compare_strings(sys.argv[1], sys.argv[2])
