#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """_summary_

    Args:
        value (_type_): _description_

    Returns:
        _type_: _description_
    """
    result = True
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as err:
        sys.stderr.write("Exception: {}\n".format(err))
        result = False
    finally:
        return result
