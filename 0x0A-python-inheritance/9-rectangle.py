#!/usr/bin/python3
"""Defining the class Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Representing rectangle via baseGeometry."""

    def __init__(self, width, height):
        """Intializing reactangle"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returning the area of rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Representation of the rectangle."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
