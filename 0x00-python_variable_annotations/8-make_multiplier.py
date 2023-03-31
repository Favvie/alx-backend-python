#!/usr/bin/env python3
"""functions annotations"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """return a function"""
    def multiply(value: float) -> float:
        """return a multiplied number"""
        return value * multiplier
    return multiply
