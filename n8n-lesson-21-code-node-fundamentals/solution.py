const items = $input.all();
const counts = {};
for (const item of items) {
  const email = item.json.email;
  counts[email] = (counts[email] || 0) + 1;
}
return items.filter(item => {
  const email = item.json.email;
  const isRepeat = counts[email] > 1;
  return item.json.total > 500 && isRepeat;
});
