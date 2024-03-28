#!/usr/bin/python3
"""
Module to the add-integer
Add two integers together

"""


def add_integer(a, b=98):
    """Return addition of a and b,
     an error if a and b are not integers/floats
    """

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    return a + b