#!/usr/bin/python3
"""Defining the JSON file-writing function."""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
