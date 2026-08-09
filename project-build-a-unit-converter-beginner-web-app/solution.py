<!DOCTYPE html>
<html>
<head>
<style>
  body { font-family: sans-serif; display: flex; justify-content: center; padding: 40px; }
  .converter { background: #1e1e2e; padding: 24px; border-radius: 12px; color: #eee; width: 280px; }
  input, select { width: 100%; margin: 8px 0; padding: 8px; border-radius: 6px; border: none; }
  #result { font-size: 1.4em; margin-top: 12px; text-align: center; }
</style>
</head>
<body>
<div class="converter">
  <input type="number" id="value" placeholder="Enter value">
  <select id="category">
    <option value="length">Length</option>
    <option value="weight">Weight</option>
    <option value="temperature">Temperature</option>
  </select>
  <select id="fromUnit"></select>
  <select id="toUnit"></select>
  <div id="result">—</div>
</div>
<script>
const units = {
  length: { m: 1, km: 1000, mi: 1609.34, ft: 0.3048, in: 0.0254, cm: 0.01, mm: 0.001, yd: 0.9144 },
  weight: { g: 1, kg: 1000, mg: 0.001, oz: 28.3495, lb: 453.592 }
};

function populate() {
  const cat = category.value;
  const list = cat === 'temperature' ? ['C','F','K'] : Object.keys(units[cat]);
  fromUnit.innerHTML = toUnit.innerHTML = list.map(u => `<option>${u}</option>`).join('');
  convert();
}

function toCelsius(v, u) {
  if (u === 'C') return v;
  if (u === 'F') return (v - 32) * 5 / 9;
  return v - 273.15;
}
function fromCelsius(c, u) {
  if (u === 'C') return c;
  if (u === 'F') return c * 9 / 5 + 32;
  return c + 273.15;
}

function convert() {
  const val = parseFloat(value.value);
  if (isNaN(val)) { result.textContent = '—'; return; }
  const cat = category.value;
  let out;
  if (cat === 'temperature') {
    out = fromCelsius(toCelsius(val, fromUnit.value), toUnit.value);
  } else {
    const base = val * units[cat][fromUnit.value];
    out = base / units[cat][toUnit.value];
  }
  result.textContent = out.toFixed(4);
}

category.addEventListener('change', populate);
value.addEventListener('input', convert);
fromUnit.addEventListener('change', convert);
toUnit.addEventListener('change', convert);
populate();
</script>
</body>
</html>
