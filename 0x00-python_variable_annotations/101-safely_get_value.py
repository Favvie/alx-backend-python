#!/usr/bin/env python3
"""type annotations"""


from typing import Any, Mapping, Union, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None] = None
                     ) -> Union[Any, T]:
    """
    Type annotated function to safely get a value from a dict"""
    if key in dct:
        return dct[key]
    else:
        return default
