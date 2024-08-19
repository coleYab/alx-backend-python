#!/usr/bin/env python3
"""
returning task for the file.
"""


import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> asyncio.Task:
    """
    Major task for creating asyncio task
    """

    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
