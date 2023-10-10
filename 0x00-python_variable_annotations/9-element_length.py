#!/usr/bin/env python3
"""9-element_length.py"""


from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """ELMENT_LENGTH"""
    return [(i, len(i)) for i in lst]
