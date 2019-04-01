#!/usr/bin/python

import unittest


def sum_double(a, b):
    """
    Given two int values, a and b, return their sum.
    Unless the two values are the same, then return double their sum.
    """
    pass


class TestSumDouble(unittest.TestCase):

    def test_1_and_2(self):
        self.assertEqual(3, sum_double(1, 2))

    def test_1_and_1(self):
        self.assertEqual(4, sum_double(1, 1))

    def test_2_and_2(self):
        self.assertEqual(8, sum_double(2, 2))

    def test_minus_1_and_2(self):
        self.assertEqual(1, sum_double(-1, 2))

    def test_minus_1_and_minus_2(self):
        self.assertEqual(-3, sum_double(-1, -2))

    def test_minus_1_and_minus_1(self):
        self.assertEqual(-4, sum_double(-1, -1))

    def test_minus_2_and_minus_2(self):
        self.assertEqual(-8, sum_double(-2, -2))


if __name__ == '__main__':
    unittest.main()
