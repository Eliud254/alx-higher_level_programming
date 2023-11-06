#!/usr/bin/python3
"""Defining rectangle subclass."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """The square."""

    def __init__(self, size):
        """Initializing square."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
