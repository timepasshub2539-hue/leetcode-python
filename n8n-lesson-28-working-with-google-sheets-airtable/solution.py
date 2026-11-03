// IF node condition
{
  "conditions": {
    "string": [{
      "value1": "={{$json.existingId}}",
      "operation": "equal",
      "value2": "={{$json.newLead.id}}"
    }]
  }
}
