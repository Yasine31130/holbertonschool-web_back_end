#!/usr/bin/env python3
"""
This is the basic_async_syntax module
"""

from random import uniform
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    Takes in an integer argument (max_delay, with a default value of 10)
    named wait_random that waits for a random delay between 0 and max_delay
    (included and float value) seconds, and returns it.
    """
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
