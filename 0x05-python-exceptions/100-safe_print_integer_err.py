#!/usr/bin/python3

import sys

def safe_print_integer_err(value):
    try:
        value = int(value)
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        print("Exception: Unknown format code 'd' for object of type '{}'".format(type(value).__name__), file=sys.stderr)
        return False
