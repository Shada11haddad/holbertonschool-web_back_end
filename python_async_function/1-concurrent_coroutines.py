#!/usr/bin/env python3
"""Run several wait_random coroutines concurrently and collect delays."""
import asyncio
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times and return delays as they complete."""
    coroutines = [wait_random(max_delay) for _ in range(n)]
    delays = []
    for finished in asyncio.as_completed(coroutines):
        delays.append(await finished)
    return delays
