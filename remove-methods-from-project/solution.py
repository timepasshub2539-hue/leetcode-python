def remainingMethods(n, k, invocations):
    graph = defaultdict(list)
    for a, b in invocations:
        graph[a].append(b)
    suspicious, stack = {k}, [k]
    while stack:
        node = stack.pop()
        for nxt in graph[node]:
            if nxt not in suspicious:
                suspicious.add(nxt); stack.append(nxt)
    for a, b in invocations:
        if a not in suspicious and b in suspicious:
            return list(range(n))
    return [i for i in range(n) if i not in suspicious]
