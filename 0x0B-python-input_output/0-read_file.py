#!/usr/bin/python3
"""Defining the text file-reading function."""


def read_file(filename=""):
    """To print  contents of a UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
