#!/usr/bin/env python3
""" duck type"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """a function that duck types an iterable object"""
    return [(i, len(i)) for i in lst]
