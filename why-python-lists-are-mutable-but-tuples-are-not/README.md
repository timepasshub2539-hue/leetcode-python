# Why Does Python Let You Edit a List But Not a Tuple?

## Problem

Two lines of Python, same shape: a variable holding a collection, and you're
adding something to it.

```python
my_list.append(4)   # works
my_tuple.append(4)  # AttributeError
```

Same intention. Wildly different outcome. Why?

## Intuition

A Python variable is a label pointing at an object in memory, not a box
holding a value. Mutable objects (like lists) expose operations that edit
their contents in place, without changing their memory address. Immutable
objects (like tuples) offer no such operation — any "change" requires
building an entirely new object.

## Approach

Prove it with `id()`:

- Append to a list → `id()` before and after is identical. Same object,
  edited in place.
- "Append" to a tuple by concatenation → `id()` changes. A new object was
  required, because tuples have no in-place mutation.

This also explains hashability: dict/set keys need a hash that never goes
stale. Immutable objects can guarantee that (hash once, valid forever).
Mutable objects can't, so Python refuses to hash them.

**Gotcha:** immutability only locks the tuple's own slots. A list nested
inside a tuple is still fully mutable.

## Python Solution

```python
def demonstrate_mutability():
    my_list = [1, 2, 3]
    list_id_before = id(my_list)
    my_list.append(4)
    list_id_after = id(my_list)

    my_tuple = (1, 2, 3)
    tuple_id_before = id(my_tuple)
    new_tuple = my_tuple + (4,)
    tuple_id_after = id(new_tuple)

    return {
        "list_same_object": list_id_before == list_id_after,
        "tuple_new_object_required": tuple_id_before != tuple_id_after,
    }


def hashable_check(value):
    try:
        hash(value)
        return True
    except TypeError:
        return False


if __name__ == "__main__":
    result = demonstrate_mutability()
    assert result["list_same_object"] is True
    assert result["tuple_new_object_required"] is True
    assert hashable_check((1, 2)) is True
    assert hashable_check([1, 2]) is False
    print("All checks passed.")
```

## Complexity

| Operation | Time | Space |
|---|---|---|
| `list.append()` | O(1) amortized | O(1) amortized |
| tuple concatenation | O(n) | O(n) |
| `hash(tuple)` | O(n) | O(1) |

## Video

(video link coming soon)

## Article

Full written breakdown with dry run, edge cases, and interview questions:
see the accompanying article in this series.
