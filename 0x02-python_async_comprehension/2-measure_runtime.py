#!/usr/bin/env python3
"""measure the time for four parallel comprehension"""

import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    "a function that measures the runtime of four parallel comprehension"
    tasks = [async_comprehension() for _ in range(4)]
    start = time.perf_counter()
    await asyncio.gather(*tasks)
    elapsed_time = time.perf_counter() - start
    return elapsed_time
