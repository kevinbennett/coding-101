#!/usr/bin/python

import unittest


def sleep_in(weekday, holiday):
    """
    The parameters weekday and holiday are booleans.
    The parameter weekday is True if it is a weekday and the parameter holiday is True if we are on holiday.
    We sleep in if it is not a weekday or we are on holiday.
    Return True if we sleep in.
    """
    pass  # TODO: Complete this function


class TestSleepIn(unittest.TestCase):

    def test_weekday_and_not_holiday(self):
        self.assertFalse(sleep_in(True, False))

    def test_not_weekday_and_not_holiday(self):
        self.assertTrue(sleep_in(False, False))

    def test_not_weekday_and_holiday(self):
        self.assertTrue(sleep_in(False, True))

    def test_weekday_and_holiday(self):
        self.assertTrue(sleep_in(True, True))


if __name__ == '__main__':
    unittest.main()
