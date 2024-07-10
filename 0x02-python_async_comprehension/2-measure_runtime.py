#!/usr/bin/env python3
import asyncio
import time
from 1-async_comprehension import async_comprehension

async def measure_runtime() -> float:
    """
    Execute async_comprehension four times in parallel using asyncio.gather.
    Measure the total runtime and return it.
    """
    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    total_time = time.perf_counter() - start_time
    return total_time
