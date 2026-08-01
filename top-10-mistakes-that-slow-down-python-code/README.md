# Why Is Your Python Code Slow?

Ten common habits that quietly wreck Python performance — explained with
intuition, code, and complexity analysis.

## Problem

Code that looks correct can still run far slower than it should, because
several common patterns (string concatenation in loops, wrong data
structures, redundant computation) hide extra work behind clean-looking
syntax.

## Intuition

Ask one question repeatedly: how much total work does this do as input
grows, and is any of it avoidable? Most slowdowns trace back to two causes —
needless copying (strings/lists rebuilt on every iteration) and needless
searching (membership checks on the wrong data structure).

## Approach

| Problem | Fix |
|---|---|
| `str += x` in a loop | Collect in a list, `"".join()` once |
| `list += [x]` in a loop | Use `.append()` / `.extend()` |
| `x in list` | Use `set`/`dict` for O(1) lookup |
| Recomputed loop-invariant value | Hoist outside the loop |
| Global/`self.` lookups | Cache in a local variable |
| Hand-written loop | Use built-ins (`map`, `sum`, `sorted`, NumPy) |
| Wrong container | Match structure to access pattern |
| Repeated deep copies | Build once outside the loop |

## Python Solution

\`\`\`python
def build_report(logs: list[str]) -> str:
    """Join unique log lines into a single report string efficiently."""
    seen: set[str] = set()
    unique_lines: list[str] = []

    for line in logs:
        if line not in seen:
            seen.add(line)
            unique_lines.append(line)

    return "\n".join(unique_lines)
\`\`\`

## Complexity

- **Time:** O(n) — set lookup/insert and list append are O(1) average case.
- **Space:** O(n) — one set, one list, bounded by input size.

## Video

Full walkthrough with a live loop-vs-built-in benchmark: (video link coming soon)

## Article

Complete write-up with dry run, edge cases, and interview questions:
(video link coming soon)
