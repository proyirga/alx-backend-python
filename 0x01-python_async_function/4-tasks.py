#!/usr/bin/python3
"""Wait N"""


import asyncio
import random
from typing import List


async def wait_random(max_delay: int = 10) -> float:
    """wait random"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

async def task_wait_random(max_delay: int) -> asyncio.Task:
    """task wait random"""
    loop = asyncio.get_event_loop()
    return loop.create_task(wait_random(max_delay))

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """task wait n"""
    delays = []
    for _ in range(n):
        task = await task_wait_random(max_delay)
        delay = await task
        delays.append(delay)
    return delays
