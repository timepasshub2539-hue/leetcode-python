# n8n Code Node: Process Every Item, Not Just the First

## Problem
n8n's Code node, when set to run once for all items, receives the entire
incoming batch — but `$json` only ever resolves to the first item in that
batch. Relying on `$json` for a multi-item transform silently drops every
row after the first, with no error thrown.

## Intuition
`$input` is the full mail tray — every item that flowed into the node.
`$json` is just the top envelope. n8n's test/pinned-data panel only ever
shows one sample item, so `$json`-based code looks correct in development
and fails silently the moment real multi-row data arrives in production.

## Approach
1. Read the full batch with `$input.all()`.
2. Transform each item with `.map()`.
3. Return each result wrapped as `{ json: {...} }` inside an array —
   n8n does not recognize unwrapped objects as valid items.

If the task is only filtering or renaming fields, use the built-in
**Filter** or **Set** node instead and skip this pattern entirely.

## JavaScript (n8n Code node)
\`\`\`javascript
const items = $input.all();

return items.map(item => ({
  json: {
    name: item.json.name.trim(),
  },
}));
\`\`\`

## Python (equivalent pattern, general batch processing)
\`\`\`python
def process_items(items: list[dict]) -> list[dict]:
    return [
        {"json": {"name": item["json"]["name"].strip()}}
        for item in items
    ]
\`\`\`

## Complexity
- Time: O(n) — every item must be visited once; this is the minimum
  possible work for a full-batch transform.
- Space: O(n) — output is a new list matching the input size, which is
  correct since one output record is produced per input record.

## Video
Full walkthrough with a live before/after run: (video link coming soon)

## Article
Full written breakdown, including the buggy version, the fix, and common
mistakes: (video link coming soon)
