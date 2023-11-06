#!/usr/bin/python3
"""Defining the base geometry and class BaseGeometry."""


class BaseGeometry:
    """Base geometry."""

    def area(self):
        """Not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Show the parameter as an integer.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
