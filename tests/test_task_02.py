#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests Task 02."""


# Import Python libs
import unittest
import hamlet
import task_02


class Task02TestCase(unittest.TestCase):
    """
    Test cases for Task 02.

    """

    def test_positional_value(self):
        """
        Tests that the POSITIONAL constant has the expected value.
        """
        monkeys = 4
        hours = 100000
        bananas = 98

        banana_effect = bananas * hamlet.BANANA_MULTIPLIER

        chance = (hours * ((monkeys / hamlet.SHIFTS) + banana_effect))
        chance /= hamlet.HAMLET_HOURS

        self.assertEqual(task_02.POSITIONAL, chance)


if __name__ == '__main__':
    unittest.main()
