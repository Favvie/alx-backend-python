#!/usr/bin/env python3
"""Tasks module"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """a function that returns the list of all the delay value"""
    delayList = []
    for i in range(n):
        delayList.append(task_wait_random(max_delay))
    return [await delay for delay in asyncio.as_completed(delayList)]
