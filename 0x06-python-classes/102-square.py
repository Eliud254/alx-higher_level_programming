#!/usr/bin/python3

"""Defining the class Square."""


class Square:
    """Representing  the square."""

    def __init__(self, size=0):
        """Initializing  the  square."""
        self.size = size

    @property
    def size(self):
        """current size of square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ current area of a square."""
        return (self.__size * self.__size)

    def __eq__(self, other):
        """To define the == comparision for the Square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """To define the != comparison of the Square."""
        return self.area() != other.area()

    def __lt__(self, other):
        """The < comparison to the Square."""
        return self.area() < other.area()

    def __le__(self, other):
        """The <= comparison to the Square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Defining the > comparison to the Square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Defining  the >= compmarison to the Square."""
        return self.area() >= other.area()
