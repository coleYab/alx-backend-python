#!/usr/bin/env python3
"""
meansuring the runtime of the wait_n coroutene
"""


import asyncio
import time
import typing
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_wait: int) -> float:
    """
    meansure_time function to meansure the total run time of a function.
    args:
        - n: total args.
        - max_wait: the maximum possible delay.
    """
    before: float = time.time()
    asyncio.run(wait_n(n, max_wait))
    after: float = time.time()

    return (after - before) / n
