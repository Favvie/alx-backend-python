#!/usr/bin/env python3
"""duck typing an iterable"""
from typing import Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """return an iterable"""
    return [(i, len(i)) for i in lst]
