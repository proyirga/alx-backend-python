#!/usr/bin/env python3
"""Multiple coroutines"""


import asyncio
from typing import List

async def wait_n(n: int, max_delay: int) -> List[float]:
    """wait random"""
    wait_random = __import__('0-basic_async_syntax').wait_random
    coroutines = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*coroutines)
    return sorted(delays)
