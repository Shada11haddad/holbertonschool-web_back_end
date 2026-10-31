#!/usr/bin/env python3
"""Measure the average runtime per coroutine when running wait_n."""
import asyncio
import time

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Return the total runtime of wait_n(n, max_delay) divided by n."""
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.perf_counter() - start
    return total_time / n
