# expenses

A command-line expense tracker built to demonstrate combining Python OOP,
testing, async concurrency, and packaging into one real, installable project.

## Problem

Track expenses across multiple currencies, total them correctly (including
the empty-ledger edge case), fetch live conversion rates without blocking on
each request, and ship the whole thing as a real command — not a script tied
to one folder.

## Intuition

Start with the plainest objects that describe the domain (`Expense`,
`Ledger`) before adding any infrastructure. Lock their behavior in with tests
before making anything faster. Only after the core is trustworthy does it
make sense to add concurrency and, finally, packaging.

## Approach

1. Model `Expense` and `Ledger` as dataclasses.
2. Write pytest tests: single add, multiple add, empty ledger.
3. Add `fetch_rate` / `attach_rates` coroutines, run concurrently via
   `asyncio.gather`.
4. Define a `pyproject.toml` entry point so `pip install .` produces a real
   `expenses` command.

## Python Solution

```python
from dataclasses import dataclass, field


@dataclass
class Expense:
    description: str
    amount: float
    currency: str = "USD"


@dataclass
class Ledger:
    expenses: list[Expense] = field(default_factory=list)

    def add(self, expense: Expense) -> None:
        self.expenses.append(expense)

    def total(self) -> float:
        return sum(e.amount for e in self.expenses)
```

## Complexity

- **Time:** O(n) to total n expenses; concurrent rate fetches are bounded by
  the slowest single request rather than the sum of all requests.
- **Space:** O(n) for expenses, O(k) for k unique currencies' rates.

## Video

Full walkthrough: (video link coming soon)

## Article

Full write-up with dry run, edge cases, and interview questions: (video link coming soon)
