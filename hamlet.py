#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module does some pretty crazy math."""

HAMLET_HOURS = 2 ** 30
SHIFTS = 3
BANANA_MULTIPLIER = 0.4


def crazy_math(monkeys, hours, typewriters=None, bananas=None):
    """This function determines the likelihood of producing Hamlet in X hours.

    Args:
        monkeys (int): Number of monkeys available.
        hours (mixed): Number of hours available to produce Hamlet.
        typewriters (int): Number of available typewriters (Optional).
        bananas (int): Number of available bananas

    Returns:
        float: The percentage likelihood of producing Hamlet as a float.

    Examples:

        >>>
    """
    if bananas is None:
        bananas = monkeys

    utilization = monkeys / SHIFTS

    if typewriters is not None and utilization > typewriters:
        utilization = typewriters

    banana_effect = bananas * BANANA_MULTIPLIER

    chance = (hours * (utilization + banana_effect)) / HAMLET_HOURS
    return chance
