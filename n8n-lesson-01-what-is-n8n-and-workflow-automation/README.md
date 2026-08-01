# What Is n8n? Nodes, Triggers & Workflows Explained

## Problem

Manually copying the same data between disconnected apps (e.g. Gmail → Sheets → Slack)
wastes time and doesn't scale. Each app holds part of the picture, but none of them
are aware the others exist.

## Intuition

Break the manual process into discrete, single-purpose steps (nodes), chain them
in the correct order (a workflow), define what starts the chain (a trigger), and
log every run (an execution) so failures are debuggable.

## Approach

1. Identify the trigger event (new email, schedule, webhook, manual click).
2. Break the process into single-responsibility nodes.
3. Chain nodes in the exact order the logic requires.
4. Log each step's output so a failed run is traceable.

## Python Solution

```python
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Execution:
    workflow_name: str
    started_at: datetime = field(default_factory=datetime.now)
    steps: list = field(default_factory=list)
    status: str = "running"

    def log_step(self, node_name: str, data: dict) -> None:
        self.steps.append({"node": node_name, "data": dict(data)})

    def finish(self, status: str = "success") -> None:
        self.status = status


def extract_lead(data: dict) -> dict:
    return {"name": data["name"], "email": data["email"]}


def add_row_to_sheet(data: dict) -> dict:
    print(f"Sheet row added: {data['name']} <{data['email']}>")
    return data


def notify_slack(data: dict) -> dict:
    print(f"Slack: New lead - {data['name']}")
    return data


def run_new_lead_workflow(trigger_data: dict) -> Execution:
    execution = Execution(workflow_name="new_lead_notification")

    data = extract_lead(trigger_data)
    execution.log_step("extract_lead", data)

    data = add_row_to_sheet(data)
    execution.log_step("add_row_to_sheet", data)

    data = notify_slack(data)
    execution.log_step("notify_slack", data)

    execution.finish("success")
    return execution


if __name__ == "__main__":
    incoming_lead = {"name": "Jordan Lee", "email": "jordan@example.com"}
    result = run_new_lead_workflow(incoming_lead)

    assert result.status == "success"
    assert len(result.steps) == 3
    print("Execution log:", result.steps)
```

## Complexity

- **Time:** O(k) per run, where k = number of nodes in the workflow.
- **Space:** O(k) for the execution log.

## Video

Watch the full lesson: (video link coming soon)

## Article

Full written breakdown with diagrams, dry runs, and interview questions: see the
main article in this repo / linked post.
