#!/usr/bin/env python3
"""1-async_comprehension.py"""


import asyncio
import random


async_generator = __import__('async_generator').async_generator


async def async_comprehension():
    """
    An async coroutine that collects 10 random numbers using
    an async comprehension over async_generator and returns them as a list.
    """
    return [await num async for num in async_generator()]
