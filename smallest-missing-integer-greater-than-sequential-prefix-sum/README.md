# Smallest Missing Integer Greater Than Sequential Prefix Sum (LeetCode 2996)

## Problem

Given an array `nums`, find the longest prefix starting at index 0 where each
value is exactly one greater than the previous value ("sequential prefix").
Sum that prefix. Return the smallest integer, greater than or equal to that
sum, that does not appear in `nums`.

## Intuition

`max(nums) + 1` is the natural first guess — and it's wrong, because it
ignores the array's actual sequential structure and any gaps within it.
Instead, track a running sum only over the initial sequential run, and use
`sum + 1` as the floor for the search. One critical edge case: if `nums[0] !=
1`, the answer is immediately `1` — the sequential-sum logic never applies.

## Approach

1. If `nums[0] != 1`, return `1`.
2. Walk the array, summing values while each one is exactly one more than
   the previous. Stop at the first break in the streak.
3. Starting from `sum + 1`, search upward for the first value not present
   in `nums`.

## Python Solution

\`\`\`python
def missing_integer(nums: list[int]) -> int:
    if nums[0] != 1:
        return 1

    total = nums[0]
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1] + 1:
            total += nums[i]
        else:
            break

    candidate = total + 1
    nums_set = set(nums)
    while candidate in nums_set:
        candidate += 1

    return candidate
\`\`\`

## Complexity

- **Time:** O(n) — one pass to compute the prefix sum, a bounded number of
  checks to find the missing value.
- **Space:** O(n) for the membership set (O(1) if checking against the list
  directly, at the cost of slower lookups on large inputs).

## Video

Full walkthrough with dry runs and quiz rounds: (video link coming soon)

## Article

Complete write-up with brute force comparison, complexity analysis, and
common mistakes: see the linked article in this repo/description.
