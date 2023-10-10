#!/usr/bin/env python3
"""101-safely_get_value.py"""


from typing import Any, Dict, Optional, TypeVar


T = TypeVar('T')

def safely_get_value(dct: Dict[Any, T], key: Any, default: Optional[T] = None) -> Optional[T]:
    """SAFELY GET VALUE"""
    if key in dct:
        return dct[key]
    else:
        return default
