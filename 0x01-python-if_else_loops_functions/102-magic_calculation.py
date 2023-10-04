#!/usr/bin/python3

# 102-magic_calculation.py

def magic_calculation(a, b, c):

    if a < b:
        return c

    if c > b:
        return a + b

    return a * b - c
