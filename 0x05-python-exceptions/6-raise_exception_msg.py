#!/usr/bin/python3
def raise_exception_msg(msg=""):
    raise NameError(msg)

try:
    raise_exception_msg("C is fun")
except NameError as ne:
    print(ne)
