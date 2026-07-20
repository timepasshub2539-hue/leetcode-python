def arrayRankTransform(arr):
    # unique values, smallest to largest
    unique_sorted = sorted(set(arr))

    # value -> rank, starting at 1
    ranks = {}
    for i, value in enumerate(unique_sorted):
        ranks[value] = i + 1
