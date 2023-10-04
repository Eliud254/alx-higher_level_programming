#!/usr/bin/python3
# 4-print_hexa.py

""" Prints numbers 0 to 98
in both decimal and hexadecimal."""
for number in range(0, 99):
    print("{} = {}".format(number, hex(number)))
