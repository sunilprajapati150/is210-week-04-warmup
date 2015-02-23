#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests Task 05."""


# Import Python libs
import unittest
import task_05


class Task05TestCase(unittest.TestCase):
    """
    Test cases for Task 05.

    """

    def test_explicit_value(self):
        """
        Tests that the keyword arguments still perform the comparison.
        """
        self.assertTrue(task_05.defaults(my_required=True, my_optional=True))
        self.assertTrue(task_05.defaults(my_required=False, my_optional=False))
        self.assertFalse(task_05.defaults(my_required=True, my_optional=False))
        self.assertFalse(task_05.defaults(my_required=False, my_optional=True))

    def test_default_value(self):
        """
        Tests that the default value is set to True and is compared to p1.
        """
        self.assertTrue(task_05.defaults(my_required=True))
        self.assertFalse(task_05.defaults(my_required=False))


if __name__ == '__main__':
    unittest.main()
