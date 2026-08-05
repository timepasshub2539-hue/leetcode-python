# n8n Editor Basics: Save vs Activate

## Problem
New n8n users don't know where core editor pieces live (canvas, node panel,
node settings, execution log), and most critically, don't understand that
saving a workflow and activating it are two separate, non-interchangeable
actions. A saved-but-not-activated workflow will not run.

## Intuition
Saving a workflow is like committing code — it records intent without
deploying it. Activating is the deploy step: it tells trigger nodes to
start listening for real events. Separating these two states lets you
freely edit and experiment without your changes going live automatically.

## Approach
1. Add nodes via the "+" button or Tab shortcut (opens a searchable,
   job-grouped panel: Triggers / Actions / Core).
2. Configure each node individually (Parameters, Credentials, Options).
3. Test each node in isolation with "Execute Node" before wiring it
   into the rest of the workflow.
4. Chain nodes — n8n auto-connects them when dropped near the last one.
5. Use the execution log to debug the full chain, node by node.
6. Save your draft, then explicitly activate when confident it's correct.

## Python Solution (conceptual analogue)

\`\`\`python
from dataclasses import dataclass
from typing import Any, Callable


@dataclass
class Step:
    name: str
    run: Callable[[Any], Any]


def execute_step(step: Step, input_data: Any) -> Any:
    try:
        result = step.run(input_data)
    except Exception as exc:
        raise RuntimeError(f"Step '{step.name}' failed: {exc}") from exc
    return result


def run_pipeline(steps: list[Step], initial_input: Any) -> Any:
    data = initial_input
    for step in steps:
        data = execute_step(step, data)
        print(f"[OK] {step.name} -> {data!r}")
    return data
\`\`\`

## Complexity
- Time: O(n) for n steps — each step runs exactly once.
- Space: O(1) beyond the data being passed through.
- Correct because each step's output is verified before becoming the
  next step's input, so failures surface immediately at their source.

## Video
Full walkthrough with the editor on screen: (video link coming soon)

## Article
Complete write-up with examples, dry run, and common mistakes: (video link coming soon)
