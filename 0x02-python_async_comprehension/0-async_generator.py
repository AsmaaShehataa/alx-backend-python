#!/usr/bin/env python3
"""Python Async Comprehntion"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Async Generator"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
