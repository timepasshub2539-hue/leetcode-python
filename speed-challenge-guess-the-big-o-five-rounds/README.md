# Big O Speed Round — 5 Time Complexity Traps

A walkthrough of five deceptively simple code snippets, each designed to test
a specific Big O assumption: nested loops, binary search, naive recursion,
and hash map lookups.

## Problem

Given five code snippets, determine the time complexity of each — and more
importantly, understand *why* that complexity holds, since several of these
snippets are built specifically to break shape-based pattern matching.

## Intuition

Don't guess Big O from what the code looks like. Guess from what actually
grows as input grows. A nested loop is only quadratic if the inner loop's
bound depends on `n`. A lookup inside a loop only adds cost if that lookup
itself scans something — a hash-based lookup doesn't.

## Approach

For each snippet, trace every loop and recursive call and ask: does this
scale with `n`, or is it bounded by a constant? Multiply out only the parts
that actually grow.

## Python Solutions

```python
def linear_scan(items, target):
    """O(n): single pass, work grows directly with input size."""
    for item in items:
        if item == target:
            return True
    return False


def bounded_inner_loop(items):
    """O(n): nested loops, but the inner loop is capped at a constant."""
    flags = ("error", "warning", "info")
    for item in items:
        for flag in flags:
            if item == flag:
                return True
    return False


def binary_search(sorted_items, target):
    """O(log n): search space halves each iteration."""
    low, high = 0, len(sorted_items) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_items[mid] == target:
            return mid
        elif sorted_items[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def naive_fibonacci(n):
    """O(2^n): each call spawns two more, recomputing identical subproblems."""
    if n <= 1:
        return n
    return naive_fibonacci(n - 1) + naive_fibonacci(n - 2)


def loop_with_hash_lookup(items, seen_set):
    """O(n): loop runs n times, but each hash lookup is O(1)."""
    for item in items:
        if item in seen_set:
            return item
    return None
```

## Complexity

| Function | Time | Space |
|---|---|---|
| `linear_scan` | O(n) | O(1) |
| `bounded_inner_loop` | O(n) | O(1) |
| `binary_search` | O(log n) | O(1) |
| `naive_fibonacci` | O(2ⁿ) | O(n) |
| `loop_with_hash_lookup` | O(n) | O(n) |

## Video

Watch the full breakdown, with a guess-before-the-reveal format for each
snippet: (video link coming soon)

## Article

Full write-up with dry runs, edge cases, common mistakes, and interview
follow-ups: (video link coming soon)
