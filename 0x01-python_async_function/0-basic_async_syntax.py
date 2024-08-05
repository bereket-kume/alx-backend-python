#!/usr/bin/env python3
"""
    this file to try async
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
        function that takes in an argument with defualt value
        and return random value that they have to wait
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
