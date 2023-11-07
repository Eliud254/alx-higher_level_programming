#!/usr/bin/python3
"""Defining the file-appending function."""


def append_write(filename="", text=""):
    """Appending the string till end of a UTF8 text file."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
