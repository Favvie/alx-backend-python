#!/usr/bin/env python3
"""a module for running coroutines concurrently"""

from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """spawn wait_random n times with max_delay"""
    tasks = []
    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)
    delays = []
    for coroutine in asyncio.as_completed(tasks):
        delay = await coroutine
        delays.append(delay)
    return delays
