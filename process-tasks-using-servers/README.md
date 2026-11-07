# LeetCode 1882 — Process Tasks Using Servers

## Problem

You're given `servers`, where `servers[i]` is the weight of server `i`, and
`tasks`, where `tasks[j]` is the duration of the task arriving at second `j`.

When a task arrives, it's assigned to the free server with the smallest
weight; ties are broken by the smallest index. If no server is free, the
task waits until one becomes available.

Return an array where `result[j]` is the index of the server that handled
task `j`.

## Intuition

The obvious-looking approach — assign task `j`, wait for it, then look at
task `j+1` — is wrong. Multiple servers can free up in the same second, and
a later task can be assigned before an earlier one if the earlier task
arrived when no server was free.

The fix: maintain two heaps.

- **Free servers**, ordered by `(weight, index)`.
- **Busy servers**, ordered by `(finish_time, index)`.

At each task, wake every server that has finished (`finish_time <= t`),
then assign the lightest, lowest-index free server.

## Approach

1. Build the free-server heap from `(weight, index)` pairs.
2. For each task at second `j`:
   - If no server is free, jump the clock to the busy heap's earliest finish time.
   - Move all servers with `finish_time <= t` from busy to free.
   - Pop the best free server, assign it, push it back onto the busy heap
     with its new finish time.

## Python Solution

```python
import heapq
from typing import List


def assign_tasks(servers: List[int], tasks: List[int]) -> List[int]:
    n = len(servers)
    avail = [(w, i) for i, w in enumerate(servers)]
    heapq.heapify(avail)
    working = []  # (finish_time, server_index)

    result = []
    for j, duration in enumerate(tasks):
        t = j
        if not avail:
            t = max(t, working[0][0])

        while working and working[0][0] <= t:
            finish_time, idx = heapq.heappop(working)
            heapq.heappush(avail, (servers[idx], idx))

        weight, idx = heapq.heappop(avail)
        heapq.heappush(working, (t + duration, idx))
        result.append(idx)

    return result
```

## Complexity

- **Time:** O((n + m) log n) — every server and task touches a heap a
  constant number of times, each operation costing O(log n).
- **Space:** O(n) for the two heaps.

## Video

Full walkthrough with a timed brute-force vs. optimal comparison: (video link coming soon)

## Article

Full written breakdown with dry run, edge cases, and interview follow-ups
available in the companion article.
