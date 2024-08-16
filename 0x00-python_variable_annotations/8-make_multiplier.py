#!/usr/bin/env python3
"""
making a multiplier closure
"""


import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """
    function to make callable that multiplies a number by other no.
    """
    return lambda mul: multiplier * mul
