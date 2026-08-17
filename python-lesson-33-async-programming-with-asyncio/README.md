# Async Web Scraper — asyncio vs Threading vs Sequential

A minimal, well-commented example demonstrating why `asyncio` outperforms
sequential requests and matches threading's speed without threading's
memory cost, for I/O-bound workloads like fetching many URLs.

## Problem

Fetching 100 URLs one at a time in a loop takes roughly the sum of every
request's round-trip time — often 60-100+ seconds — because the CPU sits
idle during each wait instead of doing anything useful with that time.

## Intuition

During a network request, the CPU isn't computing, it's parked waiting for
a response. Threading fixes this by overlapping waits across multiple
threads, but each thread reserves real memory and adds OS scheduling
overhead. `asyncio` gets the same overlap using a single thread and a
single event loop: whenever one task would block on I/O, the loop switches
to another task that's ready to run. No new threads, no new per-request
memory.

## Approach

1. Define fetch logic with `async def` so it can yield control at wait points.
2. Build a list of coroutines (not yet running) — one per URL.
3. Pass the full batch to `asyncio.gather`, which schedules and runs them
   concurrently on the single event loop.
4. Use `return_exceptions=True` to collect failures alongside successes
   instead of the first exception aborting result collection.

## Python Solution

\`\`\`python
import asyncio
import aiohttp
import time


async def fetch(session: aiohttp.ClientSession, url: str) -> str:
    async with session.get(url) as response:
        return await response.text()


async def fetch_all(urls: list[str]) -> list[str]:
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        return await asyncio.gather(*tasks, return_exceptions=True)


async def main() -> None:
    urls = [f"https://example.com/page/{i}" for i in range(100)]
    start = time.perf_counter()
    results = await fetch_all(urls)
    print(f"Fetched {len(results)} pages in {time.perf_counter() - start:.2f}s")


if __name__ == "__main__":
    asyncio.run(main())
\`\`\`

## Complexity

- **Time:** O(max(latency) + processing) instead of O(n × latency) — total
  time is bounded by the slowest single request, not the sum of all of them.
- **Space:** O(n) for task/result bookkeeping, with no per-request thread
  stack — the real cost advantage over threading is constant-factor memory,
  not asymptotic complexity.

## Video

Full walkthrough with live timing comparisons: (video link coming soon)

## Article

Full write-up with dry run, edge cases, and common mistakes: see the
accompanying article in this repo / linked from the video description.
