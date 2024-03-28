#!/usr/bin/python3
"""
Module print_square
Print the square with the character #
"""


def print_square(size):
    """Print the square where size is
    the length and width of the square
    """

    if type(size) is not int:
        raise TypeError("The size must be an integer")

    if size < 0:
        raise ValueError("The size must be >= 0")

    for i in range(size):
        for j in range(size):
            print('#', end='')
        print()