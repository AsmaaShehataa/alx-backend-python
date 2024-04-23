#!/usr/bin/env python3
"""Python Async Comprehntion"""

import asyncio
import random
from typing import List


sync_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Async Generator"""
    return [i async for i in sync_generator()]
