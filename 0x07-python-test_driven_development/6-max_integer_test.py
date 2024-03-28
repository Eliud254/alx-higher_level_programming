#!/usr/bin/python3
"""The Module to find  max integer in the list
"""


def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers
        If list is empty, the function returns None
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]#!/usr/bin/python3
"""Unittest for the max_integer module
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """The testCase for the max_integer function"""

    def test_regular(self):
        """Test with the regular list of ints: should return the max result"""
        l = [1, 2, 3, 4, 5]
        result = max_integer(l)
        self.assertEqual(result, 5)

    def test_not_int(self):
        """Test with the list of non-ints and ints:
        should raise TypeError exception"""
        l = ["a", "b", 9]
        self.assertRaises(TypeError, max_integer, l)

    def test_empty(self):
        """Test with the empty list: should return None"""
        l = []
        result = max_integer(l)
        self.assertEqual(result, None)

    def test_negative(self):
        """Test with the list of negative values: should return the max"""
        l = [-2, -6, -1]
        result = max_integer(l)
        self.assertEqual(result, -1)

    def test_float(self):
        """Test with the list of mixed ints and floats: should return the max"""
        l = [3, 4.5, 2]
        result = max_integer(l)
        self.assertEqual(result, 4.5)

    def test_not_list(self):
        """Test with the parameter that's not a list: should raise a TypeError"""
        self.assertRaises(TypeError, max_integer, 7)

    def test_unique(self):
        """Test with the list of one int: should return the value of this int"""
        l = [45]
        result = max_integer(l)
        self.assertEqual(result, 45)

    def test_identical(self):
        """Test with the list of identical values: should return the value"""
        l = [8, 8, 8, 8, 8]
        result = max_integer(l)
        self.assertEqual(result, 8)

    def test_strings(self):
        """Test with the list of strings: should return the first string"""
        l = ["hi", "hello"]
        result = max_integer(l)
        self.assertEqual(result, "hi")

    def test_none(self):
        """Test with the None as parameter: should raise a TypeError"""
        self.assertRaises(TypeError, max_integer, None)

if __name__ == '__main__':
    unittest.main()
        i += 1
    return result