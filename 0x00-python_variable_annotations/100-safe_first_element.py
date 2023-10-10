#!/usr/bin/env python3
"""100-safe_first_element.py"""


from typing import Any, List, Optional


def safe_first_element(lst: Optional[List[Any]]) -> Optional[Any]:
    """Safe First Element"""
    if lst:
        return lst[0]
    else:
        return None
