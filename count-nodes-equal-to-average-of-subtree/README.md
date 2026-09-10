# LeetCode 2265 — Count Nodes Equal to Average of Subtree

## Problem

Given the root of a binary tree, count how many nodes have a value equal to
the average of all values in their own subtree (the node itself plus every
descendant), where the average is rounded down (floor division).

## Intuition

A node's subtree is just its two children's subtrees plus itself. Instead of
re-walking each subtree from scratch for every node (O(n²)), compute each
subtree's sum and count once, bottom-up, and let parents reuse what their
children already calculated — like an org chart where each manager rolls up
numbers from direct reports instead of re-counting the whole team.

## Approach

Single postorder DFS. Each call:
1. Returns `(0, 0)` for a `None` node.
2. Recurses on left and right children first.
3. Combines: `sum = left_sum + right_sum + node.val`, `count = left_count + right_count + 1`.
4. Checks `sum // count == node.val`; increments a shared counter on match.
5. Returns `(sum, count)` to the caller.

One pass computes totals **and** performs the check.

## Python Solution

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.count = 0

        def dfs(node):
            if not node:
                return 0, 0

            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)

            total_sum = left_sum + right_sum + node.val
            total_count = left_count + right_count + 1

            if total_sum // total_count == node.val:
                self.count += 1

            return total_sum, total_count

        dfs(root)
        return self.count
```

## Complexity

| Metric | Complexity | Why |
|--------|-----------|-----|
| Time   | O(n)      | Each node visited exactly once; totals passed up, never recomputed |
| Space  | O(h)      | Recursion stack depth equals tree height |

## Video

Full walkthrough with a hand-traced example and dry run: (video link coming soon)

## Article

Complete write-up including brute force comparison, common mistakes, and
interview follow-ups: see the linked article above.
