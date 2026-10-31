#!/usr/bin/env python3
"""Create an asyncio Task that runs wait_random with a given delay."""
import asyncio

wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Return an asyncio Task that wraps wait_random(max_delay)."""
    return asyncio.create_task(wait_random(max_delay))
