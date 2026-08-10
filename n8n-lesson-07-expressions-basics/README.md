# n8n Expressions: $json vs $node

A practical breakdown of n8n's `{{ }}` expression syntax — how `$json` scopes
to the current node, when to reach for `$node` instead, and the silent-typo
failure mode that costs the most debugging time.

## Problem

n8n fields default to fixed values: whatever you type stays there forever.
Real workflows need fields that reflect live data from earlier steps instead.
Get the scoping model wrong and workflows fail silently — no error, just
wrong data flowing downstream.

## Intuition

`$json` behaves like the word "this" — it always means the data sitting at
the exact node you're in, handed off from whichever node ran immediately
before it. As an item moves from node to node, `$json` resets at every stop.
It never sees further back than its immediate parent.

`$node["Node Name"]` is the tool for reaching further upstream — it names
any earlier node directly and pulls its data regardless of how many nodes
sit in between.

## Approach

1. Click the function icon next to a field to switch it into expression mode.
2. Wrap the snippet in `{{ }}` so n8n re-evaluates it on every run.
3. Use `$json.field` for the immediate parent's data.
4. Use `$node["Name"].json.field` for anything further upstream.
5. Always check the live preview under the field before trusting the value.

## Python Solution

A minimal model of the same scoping rules, for understanding the mechanics
outside of the n8n UI:

```python
from dataclasses import dataclass, field


@dataclass
class NodeOutput:
    name: str
    json_data: dict = field(default_factory=dict)


class WorkflowContext:
    def __init__(self):
        self._history: list[NodeOutput] = []

    def run_node(self, name: str, json_data: dict) -> NodeOutput:
        output = NodeOutput(name=name, json_data=json_data)
        self._history.append(output)
        return output

    def current_json(self, field_name: str):
        if not self._history:
            raise LookupError("No node has run yet")
        return self._history[-1].json_data.get(field_name)

    def node(self, name: str, field_name: str):
        for output in self._history:
            if output.name == name:
                return output.json_data.get(field_name)
        raise LookupError(f"No node named {name!r} has run")


def demo():
    ctx = WorkflowContext()
    ctx.run_node("Node A", {"email": "maya@example.com"})
    ctx.run_node("Node B", {"signup_date": "2026-08-10"})
    ctx.run_node("Node C", {})

    assert ctx.current_json("email") is None
    assert ctx.node("Node A", "email") == "maya@example.com"
    print("All assertions passed.")


if __name__ == "__main__":
    demo()
```

## Complexity

- `current_json` (models `$json`): O(1) — only inspects the most recent node.
- `node` (models `$node["Name"]`): O(n) — scans history by name, where n is
  the number of nodes executed so far.
- Space: O(n) — every node's output is retained for the workflow's duration,
  matching n8n's actual behavior.

## Video

Full walkthrough with live examples: (video link coming soon)

## Article

Full written breakdown with dry runs, edge cases, and interview questions:
part of the *Fun with Learning Technology* series.
