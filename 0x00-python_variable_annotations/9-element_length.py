#!/usr/bin/env python3
"""
type annotation
"""


from typing import *


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Type annotated functions for py
    """
    return [(i, len(i)) for i in lst]
