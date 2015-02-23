#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests Task 04."""


# Import Python libs
import unittest
import task_04


class Task04TestCase(unittest.TestCase):
    """Test cases for Task 04."""

    testmap = {
        'not_enough_litterboxes': [2, 1, True, True],
        'plenty_of_litterboxes': [1, 2, True, False],
        'no_catfood': [1, 2, False, True],
        'same_litterboxes': [1, 1, True, False],
    }


    def test_positional_args(self):
        """
        Tests that too_many_kittens has the correct positional arguments.
        """
        for case, params in self.testmap.iteritems():
            result = task_04.too_many_kittens(*params[:3])
            msg = 'Tried {} kittens, {} litterboxes and {} food, expected {}'
            msg = msg.format(*params)
            self.assertIs(result, params[3], msg)

    def test_keyword_args(self):
        """
        Tests that too_many_kittens has the correct keyword arguments.
        """
        for case, params in self.testmap.iteritems():
            result = task_04.too_many_kittens(kittens=params[0],
                                              litterboxes=params[1],
                                              catfood=params[2])
            msg = 'Tried {} kittens, {} litterboxes, and {} food, expected {}'
            msg = msg.format(*params)
            self.assertIs(result, params[3], msg)


if __name__ == '__main__':
    unittest.main()
