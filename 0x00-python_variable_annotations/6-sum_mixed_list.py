#!/usr/bin/env python3
"""
Summing mixed lists in pyhton3
"""


import typing


def sum_mixed_list(mxd_lst: typing.Union[int, float]) -> float:
    """
    sum_mixed_list  -> adds a mixed list into float
    """
    return sum(mxd_lst)
