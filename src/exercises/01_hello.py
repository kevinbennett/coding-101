#!/usr/bin/python

import unittest


def hello(name):
    """
    Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!
    """
    pass  # TODO: Complete this function


class TestHello(unittest.TestCase):

    def test_hello_bob(self):
        self.assertEqual('Hello Bob!', hello('Bob'))

    def test_hello_alice(self):
        self.assertEqual('Hello Alice!', hello('Alice'))

    def test_hello_joe_blogs(self):
        self.assertEqual('Hello Joe Blogs!', hello('Joe Blogs'))


if __name__ == '__main__':
    unittest.main()
