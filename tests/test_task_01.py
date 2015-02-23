#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests Task 01."""


# Import Python libs
import unittest
import task_01


class Task01TestCase(unittest.TestCase):
    """
    Test cases for Task 01.

    """

    def test_documentation_length(self):
        """Tests that the function in line one has at least 11 lines.

        This assumes the absolute minimum necessary number of lines to achieve
        'complete' documentation.
        """
        numlines = len(task_01.__doc__.splitlines())
        self.assertEqual(numlines, 11, 'Expected at least 11 lines of docs.')


if __name__ == '__main__':
    unittest.main()
