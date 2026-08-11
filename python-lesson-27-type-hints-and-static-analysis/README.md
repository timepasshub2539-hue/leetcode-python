# Python Type Hints, typing, Generics, and mypy

## Problem

Python doesn't check types at runtime beyond what an operation actually
requires. A function like:

    def process(data):
        return data.upper()

will happily accept `process(42)` and only fail once `.upper()` is called
on an integer — which might be deep in a production code path.

## Intuition

A function signature is a contract. By default, Python doesn't enforce
that contract — it just runs whatever you give it. The fix is two
separate steps:

1. Declare the contract with type hints (documentation).
2. Enforce the contract with a static type checker like mypy.

Step 1 without step 2 is decoration, not safety.

## Approach

- Annotate parameters and return types: `def process(data: str) -> str:`
- Annotate variables when useful: `age: int = 25`
- Use `typing` for complex shapes: `list[int]`, `dict[str, float]`,
  `Optional[str]`, `Union[int, str]`
- Use `TypeVar` for generic functions that must stay type-consistent
  between input and output
- Run `mypy` to statically check every annotation against actual usage

## Python Solution

    from typing import Optional, TypeVar

    T = TypeVar("T")

    def process(data: str) -> str:
        return data.upper()

    def first(items: list[T]) -> T:
        return items[0]

    def find_user_name(user_id: int, users: dict[int, str]) -> Optional[str]:
        return users.get(user_id)

Run the checker:

    mypy your_file.py

## Complexity

Type hints add zero runtime overhead — they're metadata, stripped away
at execution. The real cost/benefit is developer time: mypy's static
pass catches every annotated mismatch in seconds, regardless of how
rarely that code path executes, versus an unbounded cost if the same
bug is discovered in production.

## Video

Full walkthrough: (video link coming soon)

## Article

Companion article with dry runs, edge cases, and interview questions
included in the linked write-up.
