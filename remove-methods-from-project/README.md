# LeetCode 3310 — Remove Methods From Project (Python)

## Problem

Given `n` methods and a buggy method `k`, along with `invocations` (pairs `[caller, callee]`
describing which method calls which), find every method that is safe to keep after removing
`k` and everything it calls, directly or transitively.

A method is "suspicious" if it's `k` or reachable from `k` via call edges. The suspicious
group can only be removed if no method outside the group has an edge into it — if a healthy
method still calls into the group, nothing is removed and every method is returned unchanged.

## Intuition

Two separate passes over the graph:

1. **Forward reachability** — flood fill from `k` to find every suspicious method.
2. **Reverse dependency check** — scan every edge; if a non-suspicious method calls into the
   suspicious set, block the entire removal.

## Approach

- Build an adjacency list from `invocations`.
- Iterative DFS (stack-based, not recursive) from `k` to compute the suspicious set — avoids
  Python's recursion limit on long dependency chains (`n` up to 100,000).
- One more pass over `invocations` to check for any edge crossing into the suspicious set
  from outside.
- Return all methods if blocked, otherwise return everything outside the suspicious set.

## Python Solution

```python
def remove_methods(n: int, k: int, invocations: list[list[int]]) -> list[int]:
    graph = [[] for _ in range(n)]
    for caller, callee in invocations:
        graph[caller].append(callee)

    suspicious = {k}
    stack = [k]
    while stack:
        method = stack.pop()
        for callee in graph[method]:
            if callee not in suspicious:
                suspicious.add(callee)
                stack.append(callee)

    for caller, callee in invocations:
        if callee in suspicious and caller not in suspicious:
            return list(range(n))

    return [method for method in range(n) if method not in suspicious]
```

## Complexity

- **Time:** O(n + e) — graph build, flood fill, and edge check each visit every node/edge once.
- **Space:** O(n + e) — adjacency list, suspicious set, and stack.

## Video

Full walkthrough with dry run and diagrams: (video link coming soon)

## Article

Full write-up with intuition, brute force comparison, and edge cases: (video link coming soon)
