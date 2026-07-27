# Maximum Product of Two Elements in an Array — LeetCode 1464

> Beginner-friendly. Part of the **Fun with Learning Technology** series.

## Problem

Given an array of integers `nums`, choose two **different indices** `i` and `j`
and maximize the value of `(nums[i] - 1) * (nums[j] - 1)`.

- `2 <= nums.length <= 500`
- `1 <= nums[i] <= 1000`

**Note:** the two indices must be different, but the *values* at them may be equal.

### Examples

| Input            | Output | Why                          |
|------------------|--------|------------------------------|
| `[3, 4, 5, 2]`   | `12`   | `(5-1) * (4-1) = 4 * 3`      |
| `[1, 5, 4, 5]`   | `16`   | `(5-1) * (5-1) = 4 * 4`      |
| `[2, 2]`         | `1`    | `(2-1) * (2-1) = 1 * 1`      |

## Intuition

Subtracting one and then multiplying **rewards larger inputs**. So the smallest
numbers can never contribute to the answer — you only ever need the **two
largest** values. Call it the *Top-Two Grab*.

## Approach

1. **Sort** the array ascending — the two largest values move to the end.
2. Take `nums[-1]` (largest) and `nums[-2]` (second largest).
3. Subtract one from each and multiply.

An alternative single pass tracks the top two in one scan for O(n) time.

## Python Solution

```python
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-1] - 1) * (nums[-2] - 1)
```

<details>
<summary>Single-pass O(n) version</summary>

```python
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        first = second = 0
        for num in nums:
            if num > first:
                second, first = first, num
            elif num > second:
                second = num
        return (first - 1) * (second - 1)
```
</details>

## Complexity

| Approach     | Time         | Space |
|--------------|--------------|-------|
| Brute force  | `O(n^2)`     | `O(1)`|
| Sort         | `O(n log n)` | `O(1)`|
| Single pass  | `O(n)`       | `O(1)`|

## Video

▶️ Watch the full walkthrough: (video link coming soon)

## Article

📖 Read the in-depth explanation with dry runs, edge cases, and common mistakes: (video link coming soon)

---

⭐ Star this repo if it helped, and check out the rest of the series.
