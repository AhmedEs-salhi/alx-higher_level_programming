#!/usr/bin/python3
import sys


def safe_function(func, *args):
    result = 0
    try:
        result = func(*args)
    except Exception as err:
        sys.stderr.write("Exception: {}\n".format(err))
        result = None
    finally:
        return result
