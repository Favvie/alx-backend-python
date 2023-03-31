#!/usr/bin/env python3
"""type annotations"""


def safely_get_value(dct, key, default=None):
    """get value"""
    if key in dct:
        return dct[key]
    else:
        return default
