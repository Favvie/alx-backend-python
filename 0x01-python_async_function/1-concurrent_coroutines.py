#!/usr/bin/env python3
"""
1. Let's execute multiple coroutines at the same time with async"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Return the list of all the delays (float values)"""
    delays = []
    for i in range(n):
        delays.append(wait_random(max_delay))
    return [await delay for delay in asyncio.as_completed(delays)]
