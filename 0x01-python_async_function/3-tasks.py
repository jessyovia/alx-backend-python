#!/usr/bin/env python3
"""Module for asyncio tasks"""

import asyncio
from 0-basic_async_syntax import wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    """Return an asyncio.Task"""
    return asyncio.create_task(wait_random(max_delay))
