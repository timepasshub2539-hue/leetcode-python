# Python GIL: Threading vs Multiprocessing

## Problem
Python's Global Interpreter Lock (GIL) allows only one thread to execute
Python bytecode at a time. This means threading does not provide true
parallel execution for CPU-bound work, even on multi-core machines.

## Intuition
Ask one question before choosing a concurrency tool: is the task waiting
on something external (network, disk, DB) or is it computing continuously?

- **Waiting → threading.** The GIL releases during I/O waits, so multiple
  threads' wait times overlap.
- **Computing → multiprocessing.** No idle moments means no GIL handoff,
  so threads can't overlap CPU work. Separate processes each get their
  own interpreter and GIL, enabling true parallelism across cores.

## Approach
- Use `ThreadPoolExecutor` for I/O-bound work (API calls, file reads, DB queries).
- Use `ProcessPoolExecutor` for CPU-bound work (heavy computation, tight loops).
- Both share the same `concurrent.futures` interface via `.map()`, but
  `ProcessPoolExecutor` requires all arguments/results to be picklable —
  lambdas, open file handles, and live connections will fail or misbehave.

## Python Solution

\`\`\`python
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def fetch_url(url: str) -> str:
    time.sleep(1)
    return f"fetched {url}"


def count_to_fifty_million(_: int) -> int:
    total = 0
    for i in range(50_000_000):
        total += i
    return total


def run_io_bound(urls: list[str]) -> list[str]:
    with ThreadPoolExecutor(max_workers=len(urls)) as executor:
        return list(executor.map(fetch_url, urls))


def run_cpu_bound(n_workers: int) -> list[int]:
    with ProcessPoolExecutor(max_workers=n_workers) as executor:
        return list(executor.map(count_to_fifty_million, range(n_workers)))
\`\`\`

## Complexity
| Approach | Time | Space |
|---|---|---|
| Threading (I/O-bound) | O(max wait) | O(N) thread stacks |
| Multiprocessing (CPU-bound) | O(total work / N workers) | O(N × interpreter overhead) |

## Video
Full walkthrough with live core-usage graphs: (video link coming soon)

## Article
Full written breakdown: see the accompanying article for intuition,
dry runs, and common mistakes.
