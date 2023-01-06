#!/usr/bin/python3
"""complex types - list with mixed types"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """a function that takes in a list of mixed values and returns a float"""
    sum: float = 0
    for i in mxd_lst:
        sum += float(i)
    return sum
