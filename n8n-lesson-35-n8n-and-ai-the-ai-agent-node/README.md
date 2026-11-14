# n8n AI Agent Node — Reasoning Instead of IF Chains

## Problem
Traditional n8n workflows route messages using `IF` nodes that match exact
keywords or phrases. This breaks the moment a user phrases a request in a
way the branches don't cover, and scales poorly as phrasing variety grows.

## Intuition
Replace pattern-matching with reasoning. Instead of enumerating every way a
request might be phrased, give the workflow:
- a brain (LLM) to interpret intent
- tools (hands) to act on that intent
- memory to retain context across messages

## Approach
n8n's AI Agent node requires three connections:
1. **Chat Model** — plugs into the agent's dedicated reasoning input (not a
   data line). A smaller model is often sufficient since the job is intent
   classification + action selection.
2. **Tools** — regular n8n nodes exposed to the agent. Keep each tool
   single-purpose and clearly named; overlapping tools cause misrouting.
3. **Memory** — retains conversation context across turns.

## Python Equivalent (agent loop pattern)
```python
@dataclass
class Agent:
    tools: dict[str, Tool] = field(default_factory=dict)
    memory: list[str] = field(default_factory=list)

    def handle(self, message: str, llm_call) -> str:
        self.memory.append(f"Customer: {message}")
        tool_name = self.decide_tool(message, llm_call)
        tool = self.tools.get(tool_name)
        reply = (llm_call(f"Reply using: {tool.func(message)}")
                 if tool else "I'm not sure how to help with that yet.")
        self.memory.append(f"Agent: {reply}")
        return reply
```

## Complexity
- **Time:** O(1) LLM calls per message (one tool-selection call, one
  reply-generation call), independent of tool count.
- **Space:** O(k), bounded by the memory retention window.

## Common Pitfall
Giving the agent multiple overlapping tools (e.g., "order lookup" and
"order search") degrades routing accuracy — the model can't reliably
distinguish near-duplicate tools. One tool, one job, named for what it
returns.

## Video
(video link coming soon)

## Article
Full write-up: see the linked article for intuition, dry runs, edge cases,
and common mistakes in depth.
