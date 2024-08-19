#!/usr/bin/env python3
"""
Async: abd await for the program
"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    wait_random - function to wait till the random time.
    args:
        - max_delay - maximum delay for the system.
    """
    rand_sec = random.random() * max_delay
    await asyncio.sleep(rand_sec)
    return rand_sec
