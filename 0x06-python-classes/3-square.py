#!/usr/bin/python3
"""define the square as per 2-square.py"""


class Square:
    """defining the square by size"""
    def __init__(self, size=0):
        self.__size = size
        if not isinstance(size, int):
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        """returns the area"""
        area = self.__size * self.__size
        return area
