from collections import deque
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

class Node:
    def __init__(self):
        self.children = {}
        self.fail = None
        self.outputs = []

def insert(root, word):
    node = root
    for ch in word:
        node = node.children.setdefault(ch, Node())
    node.outputs.append(word)

def build_failure_links(root):
    root.fail = root
    queue = deque(root.children.values())
    for child in queue:
        child.fail = root
    while queue:
        node = queue.popleft()
        for ch, child in node.children.items():
            queue.append(child)
            fail = node.fail
            while fail is not root and ch not in fail.children:
                fail = fail.fail
            child.fail = fail.children.get(ch, root)
            child.outputs += child.fail.outputs
    return root

def build_automaton(banned_words):
    root = Node()
    for word in banned_words:
        insert(root, word)
    return build_failure_links(root)

def search(text, root):
    node = root
    matches = []
    for i, ch in enumerate(text):
        while node is not root and ch not in node.children:
            node = node.fail
        node = node.children.get(ch, root)
        for word in node.outputs:
            start = i - len(word) + 1
            matches.append({"pattern": word, "start": start, "end": i + 1})
    return matches

BANNED_WORDS = ["spam", "scam", "crypto", "free money", "click here"]
AUTOMATON = build_automaton(BANNED_WORDS)

class ModerateRequest(BaseModel):
    text: str

app = FastAPI()

@app.post("/moderate")
def moderate(req: ModerateRequest):
    matches = search(req.text, AUTOMATON)
    return {"flagged": bool(matches), "matches": matches}

app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")
