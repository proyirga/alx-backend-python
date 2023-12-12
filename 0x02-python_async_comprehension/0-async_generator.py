#!/usr/bin/env python3
"""0-async_generator.py"""


import asyncio
import random


async def async_generator() -> AsyncGenerator[float, None]:
        """
        An async generator that yields a random number between 0.0 and 10.0 every second, 10 times.
        Yields:
           A random floating-point number between 0.0 and 10.0.
        """
        for _ in range(10):
            await asyncio.sleep(1)
            yield random.uniform(0.0, 10.0)
