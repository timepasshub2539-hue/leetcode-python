def find_valid_seq(word1, word2):
    n, m = len(word1), len(word2)
    suf = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        suf[i] = suf[i+1]
        if suf[i] < m and word1[i] == word2[m-1-suf[i]]: suf[i] += 1
    result, i, j, used = [], 0, 0, False
    while i < n and j < m:
        if word1[i] == word2[j]:
            result.append(i); i += 1; j += 1
        elif not used and suf[i+1] >= m-j-1:
            result.append(i); i += 1; j += 1; used = True
        else: i += 1
    return result if j == m else []
