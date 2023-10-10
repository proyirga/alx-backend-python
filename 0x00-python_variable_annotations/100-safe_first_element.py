#!/usr/bin/env python3
"""100-safe_first_element.py"""


from typing import List, Union


def safe_first_element(lst: List[Union[int, float, str]]) -> Union[int, float, str, None]:
    """Safe First Element"""
    if lst:
        return lst[0]
    else:
        return None
