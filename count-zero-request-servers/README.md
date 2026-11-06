# LeetCode 2747 — Count Zero Request Servers

## Problem

Given `n` servers, a log of `[server_id, time]` request entries, a window
length `x`, and a list of query times, return for each query `q` how many
servers received **zero** requests during `[q - x, q]`.

Constraints: `n`, `logs.length`, and `queries.length` can each be up to
`10^5`. `x < queries[i]` is guaranteed for every query.

## Intuition

Rescanning the full log for every query is up to `O(n_logs * n_queries)` —
too slow. Tracking a per-server last-seen timestamp is tempting but still
requires expensive per-query cleanup across all servers.

The fix: stop tracking *which* servers are silent and track *how many* are
active. `silent_count = n - active_count`. Sort logs and queries by time so
the query window only ever slides forward, then use a two-pointer sliding
window with a `count[server]` array to maintain `active_count` in place.

## Approach

1. Sort `logs` by timestamp.
2. Sort query indices by query value (preserve original index for output order).
3. Maintain `count[server]`, `active`, and pointers `left`, `right` into the sorted logs.
4. For each query `q` in time order:
   - Advance `right` through logs with `time <= q`, incrementing `count` and `active` on `0 -> 1` transitions.
   - Advance `left` through logs with `time < q - x`, decrementing `count` and `active` on `1 -> 0` transitions.
   - Answer is `n - active`, written back at the original index.

Each log entry is touched by `left` once and `right` once across the entire
run, not per query — that's what makes this fast.

## Python Solution

```python
from typing import List


def count_zero_request_servers(
    n: int,
    logs: List[List[int]],
    x: int,
    queries: List[int],
) -> List[int]:
    logs_sorted = sorted(logs, key=lambda log: log[1])
    query_order = sorted(range(len(queries)), key=lambda i: queries[i])

    answer = [0] * len(queries)
    count = [0] * (n + 1)
    active = 0
    left = right = 0
    total_logs = len(logs_sorted)

    for i in query_order:
        q = queries[i]

        while right < total_logs and logs_sorted[right][1] <= q:
            server = logs_sorted[right][0]
            if count[server] == 0:
                active += 1
            count[server] += 1
            right += 1

        while left < total_logs and logs_sorted[left][1] < q - x:
            server = logs_sorted[left][0]
            count[server] -= 1
            if count[server] == 0:
                active -= 1
            left += 1

        answer[i] = n - active

    return answer
```

## Complexity

- **Time:** `O((n_logs + n_queries) log(n_logs + n_queries))` — dominated by
  the two sorts; the sliding window itself is `O(n_logs + n_queries)`.
- **Space:** `O(n + n_logs + n_queries)`.

## Video

Full walkthrough with intuition, dry run, and a live brute-force vs. optimal
benchmark: https://youtu.be/7805RqhlB2k

## Article

Full write-up with diagrams, edge cases, and common mistakes: see the linked
article in the video description.
