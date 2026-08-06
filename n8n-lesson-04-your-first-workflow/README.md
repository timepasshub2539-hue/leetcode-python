# n8n Lesson 4: Manual Trigger + Set Node (and why the output panel goes empty)

## Problem

Build the smallest possible n8n workflow that produces real data, starting
from a completely empty canvas — and understand why an unconnected node
produces an empty output panel instead of an error.

## Intuition

n8n workflows are directed graphs. Nodes are vertices; connector lines are
edges. Execution strictly follows the edges, not the visual layout of the
canvas. A trigger is a node with no required input — the graph's starting
point. A downstream node with no incoming edge still runs, but with nothing
to process, so it produces nothing.

## Approach

1. Add a Manual Trigger node (entry point, no configuration needed).
2. Add a Set node, configured with one field: `name = "Kai"`.
3. Drag a connector line from the Trigger's output port to the Set node's
   input port — this is the step most commonly skipped.
4. Click Execute Workflow.
5. Inspect the Set node's output tab to confirm data flowed through.

## Python Model

A minimal Python model of the same execution graph, useful for
understanding the underlying logic:

\`\`\`python
class Node:
    def __init__(self, name):
        self.name = name
        self.output = None

    def run(self, input_data):
        raise NotImplementedError


class ManualTrigger(Node):
    def run(self, input_data=None):
        self.output = [{}]
        return self.output


class SetNode(Node):
    def __init__(self, name, field, value):
        super().__init__(name)
        self.field = field
        self.value = value

    def run(self, input_data):
        if input_data is None:
            self.output = []
            return self.output
        self.output = [{**item, self.field: self.value} for item in input_data]
        return self.output


def execute_workflow(edges, start_node):
    current = start_node
    data = current.run()
    while edges.get(current) is not None:
        next_node = edges[current]
        data = next_node.run(data)
        current = next_node
    return data
\`\`\`

## Complexity

- **Time:** O(n) — each node in the workflow graph executes once.
- **Space:** O(n) — output data is retained per node for downstream use
  and inspection.

## Video

Watch the full 5-minute build here: (video link coming soon)

## Article

Full written walkthrough, including the broken (unconnected) example and
detailed breakdown: (video link coming soon)
