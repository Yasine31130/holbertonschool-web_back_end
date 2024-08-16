#!/usr/bin/env python3
"""
This is the type-annotated element_length module
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    From a given iterable, returns a list of tuples with (index, length)
    where index is the index of each element and length their length.
    """
    return [(i, len(i)) for i in lst]
