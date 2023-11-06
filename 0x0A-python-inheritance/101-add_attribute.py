#!/usr/bin/python3
"""Defining the function"""


def add_attribute(obj, att, value):
    """Adding  new attribute to a object
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
