# LeetCode 2948 — Make Lexicographically Smallest Array by Swapping Elements

## Problem
Given an array of positive integers `nums` and an integer `limit`, you may
swap any two elements in the array any number of times, but only if the
absolute difference between their values is at most `limit`. Return the
lexicographically smallest array reachable through any sequence of such
swaps.

## Intuition
Swapping isn't the real operation here — connectivity is. If value A can
swap with B, and B can swap with C, then A and C belong to the same
reachable group even without a direct A-C swap. Sorting the values first
and linking adjacent values within `limit` captures every such connection
in one linear pass.

## Approach
1. Sort indices of `nums` by their values.
2. Union adjacent indices (in sorted-value order) whose values differ by
   at most `limit`.
3. Group all indices by their Union-Find root — each group is a cluster.
4. For each cluster, sort its positions and its values, then assign
   smallest value to earliest position.

## Python Solution

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            self.parent[root_x] = root_y


def lexicographically_smallest_array(nums, limit):
    n = len(nums)
    uf = UnionFind(n)
    order = sorted(range(n), key=lambda i: nums[i])

    for i in range(n - 1):
        if nums[order[i + 1]] - nums[order[i]] <= limit:
            uf.union(order[i], order[i + 1])

    clusters = {}
    for i in range(n):
        root = uf.find(i)
        clusters.setdefault(root, []).append(i)

    result = nums[:]
    for positions in clusters.values():
        positions.sort()
        values = sorted(nums[i] for i in positions)
        for pos, val in zip(positions, values):
            result[pos] = val

    return result
```

## Complexity
- **Time:** O(n log n) — dominated by the initial sort; Union-Find
  operations run in near-linear time with path compression.
- **Space:** O(n) — parent array, sorted order list, cluster groupings.

## Video
Full walkthrough with timing benchmarks and quiz checkpoints: (video link coming soon)

## Article
Complete writeup with dry run, diagrams, and complexity proof available
in the accompanying blog post.
