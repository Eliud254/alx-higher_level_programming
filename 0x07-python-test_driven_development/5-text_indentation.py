#!/usr/bin/python3
"""
Module text_indentation
Adding two new lines after a set of characters.
"""


def text_indentation(text):
    """Print text with added two newlines
    after each of these characters {'.', '?', ':'}.
    """

    if type(text) is not str:
        raise TypeError("The text must be a string")

    for delim in ".:?":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print("{}".format(text), end="")