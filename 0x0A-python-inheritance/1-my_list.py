#!/usr/bin/python3
"""Defining the inherited list of class MyList."""


class MyList(list):
    """Developing sorted printing for built-in list class."""

    def print_sorted(self):
        """To print the list sorted in ascending order."""
        print(sorted(self))
