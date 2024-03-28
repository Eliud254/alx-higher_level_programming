#!/usr/bin/python3
"""
The Module say_my_name
Print the given first name and the last name
"""


def say_my_name(first_name, last_name=""):
    """Print the string with <first_name>
    and <last_name>
    """

    if type(first_name) is not str:
        raise TypeError("The first_name must be a string")

    if type(last_name) is not str:
        raise TypeError(" The last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))