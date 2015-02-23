#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests Task 03."""


# Import Python libs
import unittest
import hamlet
import task_03


class Task03TestCase(unittest.TestCase):
    """
    Test cases for Task 03

    """

    def test_keyword_value(self):
        """
        Tests that the KEYWORD constant has the expected value.
        """
        monkeys = 84
        hours = 200000
        bananas = 48

        banana_effect = bananas * hamlet.BANANA_MULTIPLIER

        chance = (hours * ((monkeys / hamlet.SHIFTS) + banana_effect))
        chance /= hamlet.HAMLET_HOURS

        self.assertEqual(task_03.KEYWORD, chance)


if __name__ == '__main__':
    unittest.main()
