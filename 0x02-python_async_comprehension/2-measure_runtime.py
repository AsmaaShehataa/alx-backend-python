#!/usr/bin/env python3
"""Python Async Comprehension"""

import asyncio
from typing import List
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure runtime"""
    start = time.time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    end = time.time() - start
    return end
