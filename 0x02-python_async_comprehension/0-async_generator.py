#!/usr/bin/env python3
"""
    module to generate random number
"""
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
        Coroutine that generate random number using
        async generator
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
