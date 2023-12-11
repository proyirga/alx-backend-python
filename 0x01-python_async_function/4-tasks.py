#!/usr/bin/env python3
"""Multiple coroutines"""


import asyncio
from typing import List


async def task_wait_random(max_delay: int) -> float:
    """Asynchronous function that waits for a random amount of time."""
    import random
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Asynchronous function that waits for a random amount of time (task_wait_random)."""
    coroutines = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*coroutines)
    return sorted(delays)
