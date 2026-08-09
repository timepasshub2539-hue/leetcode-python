# before: manual chunking
for chunk in split_repo(size=8000):
    ask(chunk, "where's the bug?")

# after: just paste it
ask(full_repo, "where's the bug?")
