#!/usr/bin/env python3
""" sum a list"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    sum: int = 0
    for i in input_list:
        sum += i
    return sum
