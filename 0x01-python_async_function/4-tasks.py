#!/usr/bin/env python3
"""asynchronous coroutine that takes in an integer argument"""


import asyncio
import random
from typing import List
task_wait_random = __import__("tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """spawn wait_random n times with max_delay"""
    task1 = [task_wait_random(max_delay) for _ in range(n)]
    return [await t for t in asyncio.as_completed(task1)]
