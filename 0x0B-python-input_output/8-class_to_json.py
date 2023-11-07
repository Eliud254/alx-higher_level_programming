#!/usr/bin/python3
"""Defining Python class-to-JSON function."""


def class_to_json(obj):
    """Returning dictionary represntating simple data structure."""
    return obj.__dict__
