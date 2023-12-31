#!/usr/bin/env python3
"""Measure time"""


import time
import asyncio


def measure_time(n: int, max_delay: int) -> float:
    """Measure time"""
    wait_n = __import__('1-concurrent_coroutines').wait_n
    start_time = time.monotonic()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.monotonic()
    total_time = end_time - start_time
    return total_time / n
