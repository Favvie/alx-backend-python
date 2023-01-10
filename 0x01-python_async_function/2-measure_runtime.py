#!/usr/bin/env python3
"""Measure runtime"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """a function that runs total runtime and returns a float"""
    time_elapsed = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    result = time.perf_counter() - time_elapsed
    return result
