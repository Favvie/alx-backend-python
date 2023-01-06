#!/usr/bin/env python3
"""a callback function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """a function that takes a float multiplier and returns a function"""
    return lambda x: x * multiplier
