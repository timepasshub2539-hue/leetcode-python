<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Markdown Live Preview</title>
<style>
  body { margin:0; font-family: sans-serif; }
  .wrap { display:flex; height:100vh; }
  textarea, #preview { flex:1; padding:16px; box-sizing:border-box; }
  textarea { border:none; resize:none; font-size:16px; }
  #preview { overflow:auto; border-left:1px solid #ddd; }
</style>
</head>
<body>
<div class="wrap">
  <textarea id="input"></textarea>
  <div id="preview"></div>
</div>
<script>
function escapeHTML(s){return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');}
function toHTML(md){
  return escapeHTML(md)
    .replace(/^### (.*)$/gm,'<h3>$1</h3>')
    .replace(/^## (.*)$/gm,'<h2>$1</h2>')
    .replace(/^# (.*)$/gm,'<h1>$1</h1>')
    .replace(/\*\*(.+?)\*\*/g,'<b>$1</b>')
    .replace(/\*(.+?)\*/g,'<i>$1</i>')
    .replace(/`(.+?)`/g,'<code>$1</code>');
}
const input = document.getElementById('input');
const preview = document.getElementById('preview');
const saved = localStorage.getItem('md-draft');
if (saved) input.value = saved;
preview.innerHTML = toHTML(input.value);
input.addEventListener('input', () => {
  preview.innerHTML = toHTML(input.value);
  localStorage.setItem('md-draft', input.value);
});
input.addEventListener('scroll', () => {
  const pct = input.scrollTop / (input.scrollHeight - input.clientHeight);
  preview.scrollTop = pct * (preview.scrollHeight - preview.clientHeight);
});
</script>
</body>
</html>
