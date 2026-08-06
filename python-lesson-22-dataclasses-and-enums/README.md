# Python @dataclass and Enum: Killing Boilerplate and Silent Bugs

## Problem

Classes that just hold data (a cart, a point, a config) traditionally require
hand-written `__init__`, `__repr__`, and `__eq__` methods — all of it
mechanically derivable from the field list, and all of it easy to leave out
of sync when a field is added later.

## Intuition

If a computer can derive something purely from information you already typed
(field names + types), you shouldn't type it twice. `@dataclass` reads your
type-annotated class body and generates the boilerplate methods for you.

`@dataclass` solves the *shape* problem. It does not solve the *correctness*
problem — a field typed as a plain string can still be typo'd with no error.
`Enum` closes that gap by making the valid values a fixed, checked set.

## Approach

1. Decorate the class with `@dataclass`.
2. Use `field(default_factory=...)` for any mutable default (list, dict, set)
   — a literal mutable default is shared across every instance.
3. Add `frozen=True` when instances shouldn't be mutated after creation.
4. Use `Enum` for any field limited to a fixed set of named values.

## Python Solution

\`\`\`python
from dataclasses import dataclass, field
from enum import Enum, auto


class Status(Enum):
    PENDING = auto()
    ACTIVE = auto()
    DONE = auto()


@dataclass
class Cart:
    id: int
    items: list = field(default_factory=list)
    status: Status = Status.PENDING
\`\`\`

## Complexity

- **Time:** O(n) in field count for init/repr/eq — identical to a hand-written
  class, since dataclass generates that same code.
- **Space:** O(n) per instance; enum members are singletons created once at
  class-definition time, not per instance.

## Video

Full walkthrough: (video link coming soon)

## Article

Full article: (video link coming soon)
