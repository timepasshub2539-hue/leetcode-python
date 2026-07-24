# Reflexion: How AI Agents Catch Their Own Mistakes

## Problem

LLM-based agents fail confidently and silently — no error signal, just a
wrong answer stated as fact. Naive fixes either retry blindly (hoping
randomness lands differently) or require expensive fine-tuning. Neither
gives the agent a way to learn from its own specific mistake within a
session.

## Intuition

Think about writing an essay: you draft it, read it back, circle the weak
paragraph, and rewrite just that part. Reflexion does this for an AI agent,
except the agent is both the writer and the editor grading its own paper.
It splits into three roles — an actor that attempts the task, an evaluator
that scores it, and a self-reflection step that writes down the specific
lesson from any failure. That lesson feeds into the next attempt, so
retries are informed instead of random.

## Approach

1. **Actor** attempts the task.
2. **Evaluator** checks the output and returns pass/fail with a reason.
3. On failure, **self-reflection** writes a short, specific note (which
   test failed, which assumption broke).
4. The note is stored in memory (short-term for this task, optionally
   long-term across tasks) and included in the next attempt's prompt.
5. Repeat until the evaluator passes or a hard attempt cap is reached.

Two things matter most: a **hard stopping condition** (uncapped loops burn
tokens refining an already-good answer) and **specific reflections**
(vague notes like "that was wrong" are useless to the next attempt).

## Python Solution

\`\`\`python
from dataclasses import dataclass, field
from typing import Callable, Optional


@dataclass
class ReflexionResult:
    success: bool
    output: Optional[str]
    attempts: int
    reflections: list = field(default_factory=list)


def run_reflexion(
    actor: Callable[[list], str],
    evaluator: Callable[[str], Optional[str]],
    reflector: Callable[[str, str], str],
    max_attempts: int = 4,
) -> ReflexionResult:
    """
    actor(reflections) -> output
    evaluator(output) -> None if pass, else a failure description
    reflector(output, failure) -> a specific reflection note
    """
    reflections = []

    for attempt in range(1, max_attempts + 1):
        output = actor(reflections)
        failure = evaluator(output)

        if failure is None:
            return ReflexionResult(True, output, attempt, reflections)

        note = reflector(output, failure)
        reflections.append(note)

    return ReflexionResult(False, output, max_attempts, reflections)
\`\`\`

## Complexity

- **Time:** O(k) actor/evaluator calls, where k ≤ `max_attempts`.
- **Space:** O(k) to store accumulated reflections.

Both bounds hold because the loop performs exactly one actor call, one
evaluator call, and at most one reflector call per iteration, and
terminates the instant the evaluator passes or the cap is hit.

## Video

Full walkthrough with the worked example: (video link coming soon)

## Article

Full write-up with dry run, edge cases, and interview questions:
(video link coming soon)
