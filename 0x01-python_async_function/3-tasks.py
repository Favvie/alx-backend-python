#!/usr/bin/env python3
"""an async operation without an async function"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """a non-async func that return asyncio.Task"""
    task = asyncio.create_task(wait_random(max_delay))
    return task
