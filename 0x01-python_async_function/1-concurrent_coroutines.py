#!/usr/bin/python3
"""
    module that work with wait_random
"""
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay):
    """
        function that takes two argument
        n and max+delay and create list
        return list created
    """
    mylist = []
    for i in range(n):
        val = await wait_random(max_delay)
        mylist.append(val)
    return mylist
