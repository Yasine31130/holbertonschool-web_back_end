#!/usr/bin/env python3
"""
This is the task_wait_random module
"""

from asyncio import Task, create_task

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """
    Takes an integer max_delay and returns a asyncio.Task using wait_random
    """
    return create_task(wait_random(max_delay))
