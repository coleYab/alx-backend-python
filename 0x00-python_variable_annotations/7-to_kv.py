#!/usr/bin/env python3
"""
creating tuple of [str, float]
"""


import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """
    returns key: value tuple
    """
    return tuple([k, float(v ** 2)])
