#!/usr/bin/env python3
""" Run time for four parallel comprehensions """

from asyncio import gather
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Run time for four parallel comprehensions """
    debut = time()
    tasks = [async_comprehension() for x in range(4)]
    await gather(*tasks)
    fin = time()
    return (fin - debut)
