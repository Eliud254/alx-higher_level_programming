#!/usr/bin/python3
"""Defining checking function class"""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instanc """
    if type(obj) == a_class:
        return True
    return False
