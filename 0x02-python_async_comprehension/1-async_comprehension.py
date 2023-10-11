#!/usr/bin/env python3
"""1-async_comprehension.py"""


import asyncio
import random


async_generator = __import__('async_generator').async_generator


async def async_comprehension():
    """ASYNC GENERATOR"""
    return [i async for i in async_generator()]
