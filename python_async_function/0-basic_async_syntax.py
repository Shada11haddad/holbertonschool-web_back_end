#!/usr/bin/env python3
"""Basic async syntax: a coroutine that waits for a random delay."""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Wait a random delay up to max_delay seconds and return it."""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
