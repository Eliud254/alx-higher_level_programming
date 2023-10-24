#!/usr/bin/python3
"""define the  square as per 5-square.py"""


class Square:
    """implement the  square"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError('size must be an int')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        if len(position) != 2 or not isinstance(position, int) or \
           type(position) != tuple or position < 0:
            raise TypeError('position must be a tuple of 2 positive integers')

        self.__position = position

    def area(self):
        area = self.__size ** 2
        return area

    def my_print(self):
        if (self.__size == 0):
            print('')
        else:
            for i in range(self.__position[1]):
                print('')
            for i in range(self.__size):
                print(' ' * self.position[0] + '#' * self.size)
