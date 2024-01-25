#!/usr/bin/python3
"""
The module to find the hightest number in  array
"""


def find_peak(list_of_integers):
    """
    The method to find hightest number an array
    """
    if bool(list_of_integers) is False:
        return None
    list_of_integers.sort()
    return list_of_integers[-1]
