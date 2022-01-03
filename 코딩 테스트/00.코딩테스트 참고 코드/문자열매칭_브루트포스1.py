def BruteForce(t, p):
    n, m = len(t), len(p)
    i, j = 0, 0
    while i < n and j < m:
        if t[i] != p[i]:
            i = i - j
            j = -1
        i += 1
        j += 1
    if j == m:
        return i-m
    else:
        return -1
