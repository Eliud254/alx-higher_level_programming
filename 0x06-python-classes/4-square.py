#!/usr/bin/python3
"""definine the square as per 3-square.py"""


class Square:
    """definingthea square via size"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        area = self.__size * self.__size
        return area
