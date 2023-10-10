#!/usr/bin/env python3
"""0-async_generator.py"""


import asyncio
import random

async def async_generator():
    """Async generator func"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
