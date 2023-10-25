#!/usr/bin/python3

"""Defining the MagicClass as per the holberton."""

import math


class MagicClass:
    """Representing the  circle."""

    def __init__(self, radius=0):
        """Initializing the  MagicClass."""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Area of the MagicClass."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """ circumference of a MagicClass."""
        return (2 * math.pi * self.__radius)
