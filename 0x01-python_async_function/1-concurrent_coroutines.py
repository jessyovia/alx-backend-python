#!/usr/bin/env python3
"""
This module contains a coroutine that spawns multiple coroutines
"""
import asyncio
from typing import List
from random import uniform

wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay
    Returns the list of all the delays in ascending order
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
