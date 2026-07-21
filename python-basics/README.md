# Python Fundamentals: The Bug That Gets Everyone (Lists vs Tuples Explained)

## Problem
Understand Python's core building blocks — variables, data types, conditions,
loops, and functions — and the classic `=` vs `==` bug that trips up nearly
every beginner. Also covers the practical difference between lists and tuples.

## Intuition
A variable is a labeled jar holding a value; Python infers the type on its
own. Conditions are a fork in the road, decided by indentation. Loops repeat
work so you don't copy-paste code. Functions package logic for reuse, like a
coffee machine that always follows the same process on different inputs.
Lists can change after creation; tuples lock forever — choosing a tuple on
purpose protects data that should never be mutated.

## Approach
1. Store values in variables, letting Python infer the type.
2. Use `if`/`else` for decisions, based on `==` comparisons (not `=`).
3. Use `for` loops for known repetition counts, `while` for condition-driven repetition.
4. Wrap reusable logic in functions with clear inputs and outputs.
5. Choose `tuple` over `list` when the data should never change after creation.

## Python Solution
\`\`\`python
def is_even(n: int) -> bool:
    """Return True if n is even, False otherwise."""
    return n % 2 == 0


def greet(name: str) -> str:
    """Return a friendly greeting for the given name."""
    return f"Hello, {name}!"


def check_numbers(numbers: tuple) -> None:
    """Print whether each number in a fixed sequence is even or odd."""
    for n in numbers:
        result = "even" if is_even(n) else "odd"
        print(f"{n} is {result}")


if __name__ == "__main__":
    numbers = (1, 2, 3, 4)   # tuple: this sequence never changes
    check_numbers(numbers)
    print(greet("Alice"))
\`\`\`

## Complexity
- **Time:** O(n) — one pass over the input sequence.
- **Space:** O(1) — no auxiliary data structure scales with input size.

## Video
Watch the full walkthrough here: (video link coming soon)

## Article
Read the full breakdown with dry runs, common mistakes, and interview
follow-ups: (video link coming soon)
