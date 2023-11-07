#!/usr/bin/python3
"""Defining the string-to-JSON function."""
import json


def to_json_string(my_obj):
    """Returning JSON representation of the string object."""
    return json.dumps(my_obj)
