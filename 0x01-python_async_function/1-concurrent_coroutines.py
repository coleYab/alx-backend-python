#!/usr/bin/env python3
"""
1.concrrent_coroutenes.py
"""
import asyncio
import typing


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> typing.List[int]:
    """
    # wait_n
    wait_n: waits up to max_delay for n times.
    args:
        @n: total count of max_delays
        @max_delay: the max possible dealy.
    """
    wait_t = []

    for i in range(n):
        wait_t.append(await wait_random(max_delay))
        if len(wait_t) > 1:
            for i in range(len(wait_t) - 1, 0, -1):
                if wait_t[i] < wait_t[i - 1]:
                    wait_t[i], wait_t[i - 1] = wait_t[i - 1], wait_t[i]

    return wait_t
