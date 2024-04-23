#!/usr/bin/env python3
"""Python Async Comprehntion"""

import asyncio
import random
from typing import Generator


async def async_generator():
    """Async Generator"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
