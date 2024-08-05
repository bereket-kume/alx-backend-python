#!/usr/bin/env python3
"""
    module that work with wait_random
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
        function that takes two argument
        n and max-delay and create list
        return list created
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays: List[float] = []

    for i in asyncio.as_completed(tasks):
        delay = await i
        delays.append(delay)
    return delays
