#!/usr/bin/env python3
"""asynchronous coroutine that takes in an integer argument"""


import asyncio
import random

async def wait_random(max_delay: int = 10):
    """asynchronous coroutine that takes in an integer argument"""
    random_delay = random.uniform(0, max_delay)
    #wait_random = random.randrange(10, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay


