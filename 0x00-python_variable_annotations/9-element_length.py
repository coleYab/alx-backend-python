#!/usr/bin/env python3
"""
type annotation
"""


import typing


def element_length(
             lst: typing.Iterable[typing.Sequence]
        ) -> typing.List[typing.Tuple[typing.Sequence, int]]:
    """
    Type annotated functions for py
    """
    return [(i, len(i)) for i in lst]
