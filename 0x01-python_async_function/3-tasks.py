#!/usr/bin/python3
"""Task wait random"""


import asyncio
from typing import List
from random import uniform


def task_wait_random(max_delay: int) -> asyncio.Task:
    wait_random = __import__('0-basic_async_syntax').wait_random
    loop = asyncio.get_event_loop()
    return loop.create_task(wait_random(max_delay))
