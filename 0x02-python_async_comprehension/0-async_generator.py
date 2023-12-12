#!/usr/bin/env python3
"""0-async_generator.py"""


import asyncio
import random


async def async_generator():
  """
  An async generator that yields a random number between 0
  and 10 every second, 10 times.
  """
  for _ in range(10):
    await asyncio.sleep(1)
    yield random.random()*10
