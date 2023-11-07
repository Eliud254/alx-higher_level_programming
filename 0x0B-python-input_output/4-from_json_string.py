#!/usr/bin/python3
# 6-from_json_string.py
"""Defining the JSON-to-object function."""
import json


def from_json_string(my_str):
    """Returnin Python object representation for JSON string."""
    return json.loads(my_str)
