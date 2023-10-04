#!/usr/bin/python3
# 5-print_comb2.py

""" Prints numbers from 0 to 99 with specified format."""
for number in range(100):
    if number < 99:
        print("{:02d}, ".format(number), end='')
    else:
        print("{:02d}".format(number))
