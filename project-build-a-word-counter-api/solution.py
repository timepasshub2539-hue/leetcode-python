<!DOCTYPE html>
<html>
<head>
<style>
 body { font-family: sans-serif; max-width: 600px; margin: 40px auto; }
 textarea { width: 100%; height: 150px; }
 #result { margin-top: 10px; font-weight: bold; }
</style>
</head>
<body>
 <h2>Word Counter</h2>
 <textarea placeholder="Paste text here..."></textarea>
 <button>Count</button>
 <div id="result"></div>
<script>
document.querySelector('button').addEventListener('click', async () => {
  const text = document.querySelector('textarea').value;
  const res = await fetch('/count', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ text })
  });
  const data = await res.json();
  document.getElementById('result').textContent =
    `${data.words} words, ${data.characters} characters`;
});
</script>
</body>
</html>
