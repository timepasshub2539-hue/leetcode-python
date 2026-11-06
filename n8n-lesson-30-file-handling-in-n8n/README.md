# n8n: Fixing Memory Crashes on Large File Workflows

## Problem

An n8n workflow that reads a CSV, transforms it, and writes a spreadsheet
works perfectly on small test files but crashes or hangs on larger,
production-scale files — with no changes to the workflow logic itself.

## Intuition

An n8n item carries two things: a JSON body (structured data) and an
optional binary property (the attached file). By default, that binary
property holds the file's actual bytes **in memory** for the entire
workflow execution — not a reference to a file on disk. As file size
grows, memory usage grows with it, with no ceiling, until the process
runs out of RAM.

## Approach

Switch n8n's binary data storage from memory to disk using an
environment variable:

\`\`\`bash
N8N_DEFAULT_BINARY_DATA_MODE=filesystem
\`\`\`

With this set, n8n writes binary data to disk and streams it as needed
instead of holding it fully in memory. The workflow's node structure and
logic stay identical — only the underlying storage mechanism changes.

Pipeline shape (unchanged by the fix):

| Step | Node | Purpose |
|---|---|---|
| 1 | `Read Binary File` | Loads file into a binary property (now disk-backed) |
| 2 | `Extract From File` | Parses binary CSV into JSON rows |
| 3 | *(custom logic)* | Transform JSON as needed |
| 4 | `Convert to File` | Turns JSON back into a binary file |
| 5 | Write/upload node | Writes result to disk, email, or cloud storage |

For `.xlsx` files, use the `Spreadsheet File` node instead of a generic
text parser — XLSX is a zipped XML bundle, not plain text, but the
binary-in/JSON-out shape is the same.

## Python Equivalent

The same memory-vs-streaming tradeoff shows up in any data pipeline.
Minimal illustration:

\`\`\`python
import csv


def stream_from_disk(file_path: str):
    """Yields rows one at a time instead of loading the full file."""
    with open(file_path, "r", newline="", encoding="utf-8") as f:
        yield from csv.DictReader(f)
\`\`\`

## Complexity

| Approach | Time | Space |
|---|---|---|
| Load fully into memory (default) | O(n) | O(n) — scales with file size |
| Stream from disk (filesystem mode) | O(n) | O(1) — bounded regardless of file size |

Time cost is identical either way — every byte gets processed eventually.
The entire benefit is in space: streaming never holds more than a small,
constant slice of the data at once.

## Video

Full walkthrough: (video link coming soon)

## Article

Full written breakdown with examples, dry run, and edge cases: see the
companion article linked above the video.
