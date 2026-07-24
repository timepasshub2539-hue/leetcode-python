# Where Does JavaScript Actually Run?

## Problem

JavaScript executes in two distinct environments — the browser and Node.js —
and each gives the language different capabilities. Beginners often mix
these up: testing code in the browser console and expecting it to persist,
or placing a `<script>` tag before the HTML it depends on has loaded.

## Intuition

Think of JavaScript as one actor that performs on two different stages:

- **Browser stage**: an audience (the user) is watching. JavaScript can
  interact with the page — buttons, forms, DOM updates.
- **Node stage**: no audience. JavaScript runs standalone, with access to
  files, networks, and servers, but no concept of a "page" at all.

## Approach

1. Use the browser console for quick experiments only — it doesn't persist
   anything across a page refresh.
2. Write real browser code in a separate `.js` file and link it with a
   `<script>` tag rather than writing it inline, so it can be reused across
   multiple pages.
3. Place the `<script>` tag right before the closing `</body>` tag, so the
   browser has already built the page before your code runs.
4. Run standalone JavaScript with Node.js directly from the terminal — no
   browser, no HTML, no DOM involved.

## Solution

**Browser:**

\`\`\`html
<!DOCTYPE html>
<html>
<body>
  <h1>Hello</h1>
  <script src="app.js"></script>
</body>
</html>
\`\`\`

\`\`\`js
// app.js
console.log("Running inside the browser");
\`\`\`

**Node.js:**

\`\`\`js
// server.js
console.log("Running inside Node.js");
\`\`\`

\`\`\`bash
node server.js
\`\`\`

## Complexity

Not an algorithmic problem, so there's no time/space complexity to analyze.
The relevant cost is setup vs. reusability:

- Console: zero setup, zero persistence.
- Linked script: small one-time setup, reusable across every page that
  references it.
- Node execution: fixed, predictable cost per run (`node filename.js`).

## Video

Watch the full walkthrough here: (video link coming soon)

## Article

Full written lesson with examples, diagrams, and common mistakes available
on the blog/Substack.
