# n8n Workflow Version Control with Git

Treat n8n workflows as source code: export to JSON, track with git, and
promote safely between dev and prod environments.

## Problem

n8n stores every workflow as a single editable JSON blob in its database.
There's no built-in undo history — overwrite a workflow and the previous
version is gone. Manual copies (`final_v2_fixed.json`) aren't real version
control: no diffs, no authorship, no timestamps.

## Intuition

In the n8n UI, a workflow feels like a Google Doc — opaque, no diffing.
Underneath, it's plain JSON. Export it, and you have exactly the kind of
text file git was built to track.

## Approach

1. **Export** — Download the workflow as JSON from the n8n UI, or run the
   equivalent n8n CLI export command to script it.
2. **Commit & push** — Add the exported file to a git repo and commit with
   a meaningful message. This is the step that creates real history.
3. **Promote dev → prod** — Build and test changes in a separate dev n8n
   instance. Once verified, export + commit from dev, then import that
   *exact file* into prod. No rebuilding by hand.
4. **Reconnect credentials** — n8n strips credentials from every export
   for security. A clean import only confirms structure, not readiness.
   Reconnect every node's credential in prod before activating.

## Python Solution

```python
import subprocess
from pathlib import Path


def export_workflow(workflow_id: str, output_dir: Path) -> Path:
    """Export a single n8n workflow to a JSON file via the n8n CLI."""
    output_path = output_dir / f"{workflow_id}.json"
    subprocess.run(
        ["n8n", "export:workflow", "--id", workflow_id, "--output", str(output_path)],
        check=True,
    )
    return output_path


def commit_workflow(file_path: Path, message: str) -> None:
    """Stage and commit a single exported workflow file."""
    subprocess.run(["git", "add", str(file_path)], check=True)
    subprocess.run(["git", "commit", "-m", message], check=True)


def sync_workflow(workflow_id: str, output_dir: Path, message: str) -> Path:
    """Export a workflow and commit it in one step."""
    path = export_workflow(workflow_id, output_dir)
    commit_workflow(path, message)
    return path
```

## Complexity

- **Time:** O(1) per sync — export and commit both operate on current
  state, not full history.
- **Space:** Git stores diffs, not full copies, so tracking many changes
  costs far less than duplicating full JSON files per snapshot.

## Video

Full walkthrough: (video link coming soon)

## Article

Full written breakdown with examples, dry run, and common mistakes:
see the companion article in this repo / linked post.
