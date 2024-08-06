#!/usr/bin/env python3
"""
    module to generate random number
"""
import random
import asyncio
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
        function that generate random number using
        async generator
    """
    for _ in range(10):
        data = random.uniform(1, 10)
        yield data
        await asyncio.sleep(1)
