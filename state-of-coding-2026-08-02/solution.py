# this week's target
topic = "sliding window"
files = load_repo("my-service/")
prompt = build_context(files)  # ~200k tokens
answer = model.ask(prompt, "where's the race condition?")
