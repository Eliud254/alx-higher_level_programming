#!/usr/bin/python3
"""Defining the class and inherited"""


def is_kind_of_class(obj, a_class):
    """Checking if the object is a instance or inherited instance."""
    if isinstance(obj, a_class):
        return True
    return False
