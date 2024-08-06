#!/usr/bin/env python3
"""
    module to generate random number
"""
import random
import asyncio


async def async_generator():
    """
        function that generate random number using
        async generator
    """
    for i in range(1, 10):
        data = random.uniform(1, 10)
        yield data
        await asyncio.sleep(1)
