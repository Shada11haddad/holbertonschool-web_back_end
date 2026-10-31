#!/usr/bin/env python3
"""Async generator that yields ten random numbers, one per second."""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Wait 1 second, then yield a random float between 0 and 10, ten times."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
