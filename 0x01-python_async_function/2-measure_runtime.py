#!/usr/bin/env python3
"""measuring runtime"""

import asyncio
import time
wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_time: int) -> float:
    """measuring runtime"""
    start_time = time.time()
    asyncio.run(wait_n(n, max_time))
    total_time = time.time() - start_time
    return total_time / n
