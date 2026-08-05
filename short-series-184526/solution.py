total = 0
ratio = 0.5
term = 1
for _ in range(10):
    total += term
    term *= ratio
print(total)  # ~2
