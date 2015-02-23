#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests Task 04."""


# Import Python libs
import unittest
import task_04


class Task04TestCase(unittest.TestCase):
    """Test cases for Task 04."""
    pass


def create_test_positional(kittens, litterboxes, catfood, expected):
    """
    Creates and returns function objects for a test matrix of kitten tests.
    """
    def test_too_many_kittens(self):
        """
        Tests that too_many_kittens has the correct positional arguments.
        """
        result = task_04.too_many_kittens(kittens, litterboxes, catfood)
        msg = 'Tried {} kittens, {} litterboxes, and {} catfood'
        msg = msg.format(kittens, litterboxes, catfood)
        self.assertIs(result, expected, msg)
    return test_too_many_kittens


def create_test_keyword(kittens, litterboxes, catfood, expected):
    """
    Creates and returns function objects for a test matrix of kitten tests.
    """
    def test_too_many_kittens(self):
        """
        Tests that too_many_kittens has the correct keyword arguments.
        """
        result = task_04.too_many_kittens(kittens=kittens,
                                          litterboxes=litterboxes,
                                          catfood=catfood)
        msg = 'Tried {} kittens, {} litterboxes, and {} catfood'
        msg = msg.format(kittens, litterboxes, catfood)
        self.assertIs(result, expected, msg)
    return test_too_many_kittens


if __name__ == '__main__':
    TESTMAP = {
        'not_enough_litterboxes': [2, 1, True, False],
        'plenty_of_litterboxes': [1, 2, True, True],
        'no_catfood': [1, 2, False, False],
        'same_litterboxes': [1, 1, True, True],
    }

    for name, params in TESTMAP.iteritems():
        test_keyword = create_test_keyword(*params)
        setattr(Task04TestCase, 'test_keyword_{}'.format(name), test_keyword)

        test_pos = create_test_positional(*params)
        setattr(Task04TestCase, 'test_positional_{}'.format(name), test_pos)

    unittest.main()
