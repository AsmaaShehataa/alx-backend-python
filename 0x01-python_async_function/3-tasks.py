#!/usr/bin/env python3
"""tasks"""

import asyncio

measure_time = __import__("2-measure_runtime").measure_time


def task_wait_random(max_delay: int) -> asyncio.Task:
    """tasks"""
    return asyncio.create_task(measure_time(max_delay))
