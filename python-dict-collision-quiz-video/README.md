# Python Dict Collision: 1 vs True

## Problem
Given the following code:

```python
d = {}
d[1] = "one"
d[True] = "yes"
print(d)
```

What does `d` contain after both assignments?

## Intuition
Python dictionaries key on **hash equality + value equality**, not type.
Since `bool` is a subclass of `int`, `True == 1` and `hash(True) == hash(1)`.
That means `1` and `True` are the *same key* as far as a dict is concerned.

## Approach
1. `d[1] = "one"` inserts a new entry: key `1`, value `"one"`.
2. `d[True] = "yes"` hashes to the same bucket, finds `1 == True`, and
   overwrites the **value** only — the original key object (`1`) is kept.
3. The final dict has exactly one entry: `{1: 'yes'}`.

## Python Solution
```python
def demonstrate_dict_collision() -> dict:
    d = {}
    d[1] = "one"
    d[True] = "yes"
    return d


if __name__ == "__main__":
    result = demonstrate_dict_collision()
    print(result)          # {1: 'yes'}
    print(len(result))     # 1
    print(1 in result)     # True
    print(True in result)  # True
```

## Complexity
- **Time:** O(1) average per dict operation (hash table).
- **Space:** O(n) for n unique keys.

## Video
Full explanation here: (video link coming soon)

## Article
Full write-up: see the accompanying article for the complete breakdown of
Python's hash/equality contract, edge cases (`0`/`False`, `1.0`/`1`), and
common mistakes to avoid.
