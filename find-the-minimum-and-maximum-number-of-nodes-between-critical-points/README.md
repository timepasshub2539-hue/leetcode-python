# LeetCode 2058 — Find the Minimum and Maximum Number of Nodes Between Critical Points

## Problem

Given the head of a singly linked list, a **critical point** is a node that is
strictly greater than both neighbors (a local maximum) or strictly less than
both neighbors (a local minimum). Only interior nodes (with both a previous
and a next node) can be critical — the head and tail never qualify.

Return `[min_distance, max_distance]` between critical points in the list.
If there are fewer than two critical points, return `[-1, -1]`.

## Intuition

The maximum distance is always the gap between the **first** and **last**
critical point — nothing in between can be farther apart than the two
extremes. The minimum distance is local: only ever compare a critical point
to the one immediately before it. One value is global, the other is local —
track `first`, `prev`, and `last` in a single pass and you're done.

## Approach

1. Walk the list with two pointers (`prev`, `curr`), one step apart.
2. At each `curr` (while `curr.next` exists), check if it's a peak or valley.
3. On the first critical point found, record its index as `first`.
4. On every subsequent one, update `min_dist` against the gap from the
   previous critical point, then update `prev_idx` and `last`.
5. After the loop, if fewer than two critical points were found, return
   `[-1, -1]`. Otherwise return `[min_dist, last - first]`.

## Python Solution

```python
from typing import Optional, List


class ListNode:
    def __init__(self, val: int = 0, next: 'Optional[ListNode]' = None):
        self.val = val
        self.next = next


def nodes_between_critical_points(head: Optional[ListNode]) -> List[int]:
    prev = head
    curr = head.next
    idx = 1

    first = prev_idx = last = None
    min_dist = float('inf')

    while curr and curr.next:
        is_peak = curr.val > prev.val and curr.val > curr.next.val
        is_valley = curr.val < prev.val and curr.val < curr.next.val

        if is_peak or is_valley:
            if first is None:
                first = idx
            else:
                min_dist = min(min_dist, idx - prev_idx)
            prev_idx = idx
            last = idx

        prev = curr
        curr = curr.next
        idx += 1

    if first is None or first == last:
        return [-1, -1]

    return [min_dist, last - first]
```

## Complexity

- **Time:** O(n) — single pass over the list.
- **Space:** O(1) — a fixed set of scalar trackers, no auxiliary data structures.

## Video

Full derivation, live trace, and two in-video quizzes: (video link coming soon)

## Article

Full written breakdown with dry run, edge cases, and common mistakes: see the
accompanying article in this repo / linked from the video description.
