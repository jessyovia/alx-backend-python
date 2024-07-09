#!/usr/bin/env python3
"""Module to handle multiple tasks"""

import asyncio
from typing import List
from 3-tasks import task_wait_random

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn task_wait_random n times and return list of delays"""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
