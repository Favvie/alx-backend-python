#!/usr/bin/env python3
"""an async comprehension module"""

from typing import List
import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    values = [i async for i in async_generator()]
    return values
