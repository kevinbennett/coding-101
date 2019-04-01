#!/usr/bin/python

import unittest


def near_one_or_two_hundred(number_to_check):
    """
    Given an int number_to_check, return True if it is within 10 of 100 or 200.
    Note: abs(num) computes the absolute value of a number.
    """
    pass


class TestNear(unittest.TestCase):

    def test_89(self):
        self.assertFalse(near_one_or_two_hundred(89))

    def test_90(self):
        self.assertTrue(near_one_or_two_hundred(90))

    def test_110(self):
        self.assertTrue(near_one_or_two_hundred(110))

    def test_111(self):
        self.assertFalse(near_one_or_two_hundred(111))

    def test_189(self):
        self.assertFalse(near_one_or_two_hundred(189))

    def test_190(self):
        self.assertTrue(near_one_or_two_hundred(190))

    def test_210(self):
        self.assertTrue(near_one_or_two_hundred(210))

    def test_211(self):
        self.assertFalse(near_one_or_two_hundred(211))


if __name__ == '__main__':
    unittest.main()
