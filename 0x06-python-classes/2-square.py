#!/usr/bin/python3
""" The class square defination on 1-square.py"""


class Square:
    """initialize the size """
    def __init__(self, size=0):
        """initialize the new square"""
        self.__size = size
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
