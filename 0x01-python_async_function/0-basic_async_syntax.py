#!/usr/bin/env python3
""" asynchronous coroutine using random module"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Wait for a random delay between 0 and max_delay seconds and return it"""
    delayValue = random.uniform(0, max_delay)
    await asyncio.sleep(delayValue)
    return delayValue
