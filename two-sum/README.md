# Two Sum — Python Solution

## Problem

Given an array of integers `nums` and an integer `target`, return the indices
of the two numbers that add up to `target`.

- Exactly one valid pair is guaranteed to exist.
- You may not use the same array element twice.
- Return the indices in any order.

## Intuition

Instead of checking every pair (`does this number match anything else?`),
flip the question: for each number, ask what value would need to already
exist to complete the pair (`target - number`). Track everything you've
seen in a dictionary, so that question becomes a single lookup instead of
a rescan.

## Approach

1. Walk the array once.
2. For each value, compute its complement: `target - value`.
3. If the complement is already in the dictionary, return its stored index
   and the current index.
4. Otherwise, store the current value and its index, and continue.

Checking the dictionary *before* inserting the current value is what
prevents an element from being paired with itself.

## Python Solution

```python
def two_sum(nums: list[int], target: int) -> list[int]:
    """Return indices of the two numbers that add up to target."""
    seen = {}  # value -> index

    for index, value in enumerate(nums):
        complement = target - value
        if complement in seen:
            return [seen[complement], index]
        seen[value] = index

    raise ValueError("no two sum solution found")
```

## Complexity

| Approach    | Time  | Space |
|-------------|-------|-------|
| Brute force | O(n²) | O(1)  |
| Hash map    | O(n)  | O(n)  |

Brute force rescans the array for every element. The hash map trades O(n)
space for a single pass, turning each lookup into an average O(1) operation.

## Video

Full walkthrough, including a live timed comparison of both approaches:
(video link coming soon)

## Article

Complete written breakdown with dry run, edge cases, and interview
follow-ups: (video link coming soon)
