#!/usr/bin/env python3
"""101-safely_get_value.py"""


from typing import Any, Mapping, Union, TypeVar


T = TypeVar('T')

def safely_get_value(dct: Mapping, key: Any, default: Union[Any, T] = None) -> Union[Any, T]:
    """SAFELY GET VALUE"""
    if key in dct:
        return dct[key]
    else:
        return default
