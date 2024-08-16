#!/usr/bin/env python3
"""
This is the basic_async_syntax module
"""

from asyncio import run
from time import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay), and
    returns the average subroutine execution time
    """
    starting_time = time()
    run(wait_n(n, max_delay))
    ending_time = time()

    return ((ending_time - starting_time) / n)
