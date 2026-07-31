# Binary Search in Python

## Problem

Given a sorted array of integers and a target value, return the index of the
target if it exists, or -1 if it doesn't.

## Intuition

If the array is sorted, checking the middle element tells you more than
"is this the target?" — it tells you which half of the array can be
eliminated entirely. Repeating this halves the search space every step,
which is why the number of steps needed grows logarithmically instead of
linearly with the size of the array.

## Approach

1. Track the current search range with `low` and `high`.
2. Compute `mid`, the midpoint of the range.
3. Compare `array[mid]` to the target:
   - Match → return `mid`.
   - Target is larger → search the right half (`low = mid + 1`).
   - Target is smaller → search the left half (`high = mid - 1`).
4. Repeat until `low > high` (no range left), then return `-1`.

## Python Solution

\`\`\`python
def binary_search(array: list[int], target: int) -> int:
    """Return the index of target in a sorted array, or -1 if absent."""
    low, high = 0, len(array) - 1

    while low <= high:
        mid = (low + high) // 2

        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


if __name__ == "__main__":
    data = [2, 5, 8, 13, 21, 27, 33, 41, 50, 67]
    assert binary_search(data, 33) == 6
    assert binary_search(data, 2) == 0
    assert binary_search(data, 67) == 9
    assert binary_search(data, 100) == -1
    assert binary_search([], 5) == -1
    print("All tests passed.")
\`\`\`

## Complexity

- **Time:** O(log n) — each step halves the search range.
- **Space:** O(1) — iterative, constant extra memory.

## Video

Full walkthrough with hand-traced examples and a live run: (video link coming soon)

## Article

Full written breakdown with dry runs, edge cases, and interview follow-ups:
(video link coming soon)
