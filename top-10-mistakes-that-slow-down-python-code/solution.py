for i in range(len(data)):
    if data[i] > threshold * 2:
        process(data[i])

# better
limit = threshold * 2
n = len(data)
for i in range(n):
    if data[i] > limit:
        process(data[i])
