#!/usr/bin/env python3
"""
    module for async_comprehension
"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
        async_comprehension is function that create
        list of random number form async_genertor module
        and return all values
    """
    values = [value async for value in async_generator()]
    return values
