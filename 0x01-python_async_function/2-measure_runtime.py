#!/usr/bin/env python3
"""measuring runtime"""

import asyncio
from time import perf_counter
wait_n = __import__("1-concurrent_coroutines").wait_n


async def measure_time(n: int, max_time: int) -> float:
    """measuring runtime"""
    start_time = perf_counter()
    asyncio.run(wait_n(n, max_time))
    elapsed = perf_counter() - start_time
    return elapsed / n
