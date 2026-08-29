const items = $input.all();

return items.map(item => {
  const clean = item.json.name.trim();

  return {
    json: {
      name: clean
    }
  };
});
