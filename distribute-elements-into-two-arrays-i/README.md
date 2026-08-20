# LeetCode 3069 — Distribute Elements Into Two Arrays I (Python)

## Problem

Given a 1-indexed array `nums` of distinct integers, distribute every element
into one of two arrays, `arr1` or `arr2`, using this rule:

- The first element always goes to `arr1`.
- The second element always goes to `arr2`.
- Every element after that goes to whichever array currently ends with the
  larger value.

Return `arr1` concatenated with `arr2`.

## Intuition

The decision only ever depends on the *last* element of each array — never
on sums, sizes, or overall value order. That rules out sorting or a heap:
you need O(1) access to a tail, which a plain Python list already gives you.

## Approach

1. Seed `arr1` with `nums[0]`, `arr2` with `nums[1]` (avoids ever comparing
   against an empty list).
2. Loop through the rest of `nums`, comparing `arr1[-1]` and `arr2[-1]`.
3. Append each number to whichever array is currently ahead.
4. Return `arr1 + arr2`.

## Python Solution

\`\`\`python
from typing import List


class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = [nums[0]]
        arr2 = [nums[1]]

        for num in nums[2:]:
            if arr1[-1] > arr2[-1]:
                arr1.append(num)
            else:
                arr2.append(num)

        return arr1 + arr2
\`\`\`

## Complexity

- **Time:** O(n) — one pass, one comparison per element.
- **Space:** O(n) — for the two output arrays.

## Video

Full walkthrough: (video link coming soon)

## Article

Full write-up with dry run, complexity analysis, and common mistakes:
see the linked article above.
