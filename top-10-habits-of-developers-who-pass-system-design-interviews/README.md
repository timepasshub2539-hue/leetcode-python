# System Design Interview Habits: A Repeatable Process

## Problem

Given an open-ended prompt ("design Twitter," "design a chat app"), produce a
scalable system design while narrating your reasoning, in roughly 30-45
minutes, with no single correct answer.

## Intuition

Don't scale for problems you haven't confirmed exist. Start with the simplest
system that could work, and add complexity only when you can name the exact
bottleneck it solves. This round evaluates process and communication, not a
memorized architecture.

## Approach

1. **Clarify** — ask about scale, read/write ratio, and latency tolerance
   before designing anything.
2. **Start simple** — one client, one server, one database. State out loud
   what breaks first as load increases.
3. **Scale on purpose** — add a cache, shard, or queue only after naming the
   specific bottleneck it addresses.
4. **Eliminate single points of failure** — a second server behind a load
   balancer.
5. **Separate sync from async** — critical-path writes stay synchronous;
   secondary updates (like feed fan-out) move to a queue.
6. **Manage depth** — cover the whole system shallowly before going deep on
   any one part.
7. **Be honest about gaps** — "I'm not sure of the exact number, here's how
   I'd find out" beats a confident wrong guess.

## Python Solution

```python
from typing import Callable, Optional
import time


class ReadThroughCache:
    """A simple in-memory cache that falls back to a data source on miss."""

    def __init__(self, ttl_seconds: int = 60):
        self._store: dict[str, tuple[float, object]] = {}
        self._ttl = ttl_seconds

    def get(self, key: str, fetch_fn: Callable[[str], object]) -> object:
        cached = self._store.get(key)
        if cached is not None:
            expires_at, value = cached
            if time.monotonic() < expires_at:
                return value  # cache hit

        value = fetch_fn(key)
        self._store[key] = (time.monotonic() + self._ttl, value)
        return value

    def invalidate(self, key: str) -> None:
        self._store.pop(key, None)
```

## Complexity

- **Time:** O(1) for cache hits; cost of `fetch_fn` (typically O(log n) for
  an indexed DB lookup) on a miss.
- **Space:** O(k), where k is the number of unique keys currently cached
  within the TTL window.

## Video

Full walkthrough with live narration: (video link coming soon)

## Article

Full written breakdown, including the four-step scaling sequence, dry run,
and common mistakes: see the article above.
