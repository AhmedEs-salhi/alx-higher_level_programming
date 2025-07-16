import sys

def compare_strings(string_1, string_2):
    if string_1 == string_2:
        return True
    return False
compare_strings(sys.argv[2], sys.argv[3])
