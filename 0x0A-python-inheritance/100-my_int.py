#!/usr/bin/python3
"""Defining the class MyInt"""


class MyInt(int):
    """Inverting the  int operators == and !=."""

    def __eq__(self, value):
        """Override == opeartor via != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Override != operator via == behavior."""
        return self.real == value
