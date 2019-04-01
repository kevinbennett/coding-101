#!/usr/bin/python

import unittest


def front_back(string):
    """
    Given a string, return a new string where the first and last characters have been swapped.
    If the string is empty or only has one character then return the string unchanged.
    """
    pass


class TestFrontBack(unittest.TestCase):

    def test_hello(self):
        self.assertEqual('oellh', front_back('hello'))

    def test_goodbye(self):
        self.assertEqual('eoodbyG', front_back('Goodbye'))

    def test_a(self):
        self.assertEqual('a', front_back('a'))

    def test_aa(self):
        self.assertEqual('aa', front_back('aa'))


if __name__ == '__main__':
    unittest.main()
