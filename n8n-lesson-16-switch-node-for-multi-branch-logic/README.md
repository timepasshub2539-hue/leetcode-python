# n8n Switch Node vs. Nested IF Nodes

## Problem
Routing an item to more than two destinations using only IF nodes forces you into
a pyramid of nested conditionals — one IF inside another, growing deeper with
every new rule. It's structurally the same as chaining `elif` statements in code,
and it becomes unreadable fast.

## Intuition
An IF node is a binary decision: true or false, one of two outputs. It was never
designed to hand an item to more than two places. The fix isn't a workaround —
it's using a node built for multi-way routing. n8n's Switch node does exactly
that: one input, as many outputs as needed, one rule per output.

## Approach
- Each Switch rule = field to read + condition to satisfy + output label.
- Rules evaluate **top to bottom**, first-match-wins (like a `switch` statement
  with implicit breaks) — not "every matching rule fires."
- A built-in **fallback output** catches items that match nothing.
- Use IF when there are genuinely only two outcomes — Switch adds no value there.

## Python Solution

\`\`\`python
def route_ticket(ticket_type: str, rules: list[tuple[str, str]], fallback: str = "unrouted") -> str:
    """First-match-wins router, mirroring n8n's Switch node semantics."""
    for expected_value, output_label in rules:
        if ticket_type == expected_value:
            return output_label
    return fallback


ticket_rules = [
    ("refund", "Refund"),
    ("billing", "Billing"),
    ("technical", "Technical"),
    ("complaint", "Complaint"),
]

assert route_ticket("refund", ticket_rules) == "Refund"
assert route_ticket("unknown", ticket_rules) == "unrouted"
\`\`\`

## Complexity
- **Time:** O(n) — worst case scans every rule once.
- **Space:** O(1) — no auxiliary structure beyond the input.
- A dict-based lookup can reach O(1) average case, but only for pure equality
  rules with no overlap — it loses explicit ordering semantics that matter
  once rules can match the same item.

## Video
Watch the full walkthrough: (video link coming soon)

## Article
Full write-up with diagrams, dry run, and edge cases: see the linked article above.
