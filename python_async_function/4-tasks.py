#!/usr/bin/env python3
"""
This is the task_wait_n module
"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Async routine that takes in 2 int arguments (n, max_delay) and
    populates a list with n task_wait_random return values.
    Returns the list of all the delays (float values).
    """
    delays = []

    async def wait_and_store(delay: int, result_list: List[float]):
        """
        Subroutine function that appends the task_wait_random return value
        to the list after waiting.
        """
        result_list.append(await task_wait_random(delay))

    tasks = [wait_and_store(max_delay, delays) for _ in range(n)]
    await asyncio.gather(*tasks)

    return delays
