#!/usr/bin/env python3
"""a non-async function module"""

from typing import List
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    tasks = []
    for _ in range(n):
        task = task_wait_random(max_delay)
        tasks.append(task)
    delays = []
    for coroutine in asyncio.as_completed(tasks):
        delay = await coroutine
        delays.append(delay)
    return delays
