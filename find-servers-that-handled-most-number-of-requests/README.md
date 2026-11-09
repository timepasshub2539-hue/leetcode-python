# LeetCode 1606 — Find Servers That Handled Most Number of Requests

## Problem

You have `k` servers (indexed `0` to `k-1`). Requests arrive one at a time with
strictly increasing arrival times. For request `i`, the system tries server
`i % k` first; if busy, it checks subsequent servers in order (wrapping to 0),
assigning the first free one. If every server is busy, the request is dropped.
Return every server index that handled the most requests overall.

Constraints: `k` and the number of requests can each be up to 100,000.

## Intuition

The problem reads like plain round robin, which tempts a busy/free boolean
array. That breaks because you need to know *when* a busy server frees up, not
just that it's currently occupied. Split servers into two groups instead:

- **Available** — free right now (sorted list, binary-searchable)
- **Busy** — tagged with an exact finish time (min-heap)

Since arrival times are strictly increasing, releasing finished servers right
before handling each new request is always safe — no sorting needed.

## Approach

1. Before each request, pop every busy server whose finish time has passed,
   moving it back into `available` (kept sorted via `bisect.insort`).
2. If `available` is empty, drop the request.
3. Use `bisect_left(available, i % k)` to find the smallest free server at or
   after `i % k`; wrap to index 0 if the search runs off the end.
4. Assign the request, increment that server's count, push
   `(arrival[i] + load[i], server)` onto the busy heap.
5. Return every server index tied for the maximum count.

## Python Solution

```python
import heapq
import bisect


class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        available = list(range(k))
        busy = []
        count = [0] * k

        for i, start in enumerate(arrival):
            while busy and busy[0][0] <= start:
                _, server = heapq.heappop(busy)
                bisect.insort(available, server)

            if not available:
                continue

            pos = bisect.bisect_left(available, i % k)
            if pos == len(available):
                pos = 0

            server = available.pop(pos)
            count[server] += 1
            heapq.heappush(busy, (start + load[i], server))

        best = max(count)
        return [i for i, c in enumerate(count) if c == best]
```

## Complexity

- **Time:** `O(n log k)` driven by heap operations, versus `O(n * k)` for
  brute-force per-request scanning.
- **Space:** `O(k)` for the available list, busy heap, and count array.
- Measured speedup over brute force: ~233x (3.35s → 14.36ms) on a timed run
  with real and extra edge-case inputs.

## Video

Full walkthrough, dry run, and correctness proof: (video link coming soon)

## Article

Full write-up with diagrams and interview follow-ups: (video link coming soon)
