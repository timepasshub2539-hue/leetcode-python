# Functional vs Non-Functional Requirements — Why Systems Fail in Production

A companion write-up and code sample for the Fun with Learning Technology
software architecture series, Lesson 2.

## Problem

A system can pass every functional test — every feature works exactly as
specified — and still fail in production. This happens when non-functional
requirements (latency, scale, availability) are never written down, so the
architecture is never designed to meet them.

## Intuition

Every requirement answers one of two questions:

- **What must the system do?** → functional requirement (a feature, checked
  off yes/no)
- **How well must it do it?** → non-functional requirement (a number:
  latency, concurrent users, uptime)

Functional requirements describe *what* to build. Non-functional
requirements determine *how* to build it — they're the actual architectural
constraints, even though they never appear on a feature list.

## Approach

1. List every feature as a functional requirement.
2. Attach concrete numbers to each: expected concurrent users, target
   latency, required availability.
3. Let those numbers — not the feature list — drive architecture decisions
   (single server vs. load balancer + multiple servers, plain database vs.
   caching/indexing/search engine).
4. Validate the design against the numbers before launch, not after.

Example — same feature, different architecture:

| | System A | System B |
|---|---|---|
| Feature | Search for a product | Search for a product |
| Users | 100 | 10,000,000 |
| Latency target | 2s | 50ms |
| Architecture | Single database | Caching + indexing + search engine (e.g. Elasticsearch) |

## Python Solution

```python
from dataclasses import dataclass
from typing import Optional


@dataclass
class FunctionalRequirement:
    name: str
    description: str


@dataclass
class NonFunctionalRequirement:
    max_latency_ms: Optional[int] = None
    min_availability_pct: Optional[float] = None
    concurrent_users: Optional[int] = None

    def describe(self) -> str:
        parts = []
        if self.concurrent_users is not None:
            parts.append(f"{self.concurrent_users:,} concurrent users")
        if self.max_latency_ms is not None:
            parts.append(f"under {self.max_latency_ms}ms response")
        if self.min_availability_pct is not None:
            parts.append(f"{self.min_availability_pct}% availability")
        return ", ".join(parts) if parts else "no constraints specified"


@dataclass
class Feature:
    functional: FunctionalRequirement
    non_functional: NonFunctionalRequirement

    def needs_horizontal_scaling(self) -> bool:
        return (self.non_functional.concurrent_users or 0) > 1000

    def needs_low_latency_infra(self) -> bool:
        return (self.non_functional.max_latency_ms or float("inf")) < 100


def summarize(feature: Feature) -> str:
    nfr = feature.non_functional.describe()
    flags = []
    if feature.needs_horizontal_scaling():
        flags.append("load balancer + multiple servers")
    if feature.needs_low_latency_infra():
        flags.append("caching / indexing / search engine")

    flags_str = f" -> requires: {', '.join(flags)}" if flags else " -> single server is fine"
    return f"{feature.functional.name} ({nfr}){flags_str}"


def demo():
    system_a = Feature(
        FunctionalRequirement("Search for a product", "..."),
        NonFunctionalRequirement(max_latency_ms=2000, concurrent_users=100),
    )
    system_b = Feature(
        FunctionalRequirement("Search for a product", "..."),
        NonFunctionalRequirement(max_latency_ms=50, concurrent_users=10_000_000),
    )

    assert "single server is fine" in summarize(system_a)
    assert "load balancer" in summarize(system_b)
    assert "search engine" in summarize(system_b)
    print(summarize(system_a))
    print(summarize(system_b))


if __name__ == "__main__":
    demo()
```

## Complexity

- Time: O(1) per feature evaluated — fixed number of threshold checks.
- Space: O(1) per feature — constant number of stored fields.
- Note: the complexity of this code is trivial by design. The complexity
  it's pointing at (load balancers, caching layers, distributed search)
  belongs to the *system*, not the analysis — which is the whole lesson.

## Video

Full walkthrough with the System A vs. System B comparison: (video link coming soon)

## Article

Full written lesson with dry run, edge cases, and interview questions:
(video link coming soon)
