#!/usr/bin/env python3
"""Async"""


import asyncio
import random


async_comprehension = __import__('async_generator')


async def measure_runtime():
    """Measure runtime"""
    start_time = asyncio.get_running_loop().time()
    await asyncio.gather(async_comprehension(), async_comprehension(), async_comprehension(), async_comprehension())
    end_time = asyncio.get_running_loop().time()
    return end_time - start_time
