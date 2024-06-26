#!/usr/bin/env python3
"""Concurrent coroutines"""

import asyncio
import random
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """spawn wait_random n times with max_delay"""
    task1 = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await t for t in asyncio.as_completed(task1)]
