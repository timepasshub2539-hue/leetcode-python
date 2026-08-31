# n8n: Execute Workflow Node for Reusable Sub-Workflows

## Problem
An 8-node Slack alert cluster was copy-pasted into 12 separate n8n workflows.
A single formatting change required manually editing all 12 — with real risk
of missing some. A bug in the cluster existed independently in every copy.

## Intuition
Same principle as extracting a shared function in any codebase: build the
logic once, have every caller reference that single copy instead of owning
an independent version. Like a saved phone contact — update it once, every
group chat referencing it sees the change.

## Approach
1. Move the repeated node cluster into its own standalone workflow.
2. Set that workflow's trigger to **"When Executed by Another Workflow"**
   (not Manual, not Schedule — this is the most common setup mistake).
3. In each caller workflow, add an **Execute Workflow** node pointing its
   Source at the sub-workflow.
4. Map inputs/outputs via the Execute Workflow node's **Workflow Inputs** tab.

## Python Analogy
```python
def send_slack_alert(payload):
    """Single source of truth — every caller invokes this instead of
    reimplementing the logic inline."""
    channel_id = resolve_channel(payload.channel)
    formatted = format_message(payload.message)
    return post_to_slack(channel_id, formatted)
```

## Complexity
- Change propagation: O(1) edit vs. O(n) manual edits across n workflows.
- Maintenance surface: 1 implementation vs. n independent duplicates.

## Video
Full walkthrough: (video link coming soon)

## Article
Full write-up (intuition, code walkthrough, edge cases, common mistakes):
see the linked article above.
