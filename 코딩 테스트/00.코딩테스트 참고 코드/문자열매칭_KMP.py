# Failure Function
def makeTable(pattern):
    m = len(pattern)
    tb = [0 for _ in range(m)]

    pidx = 0
    for idx in range(1, m):
        while pidx > 0 and pattern[idx] != pattern[pidx]:
            pidx = tb[pidx-1]
        if pattern[idx] == pattern[pidx]:
            pidx += 1
            tb[idx] = pidx

    return tb


# KMP 알고리즘
def KMP(word, pattern):
    table = makeTable(pattern)

    results = []
    pidx = 0
    for idx in range(len(word)):
        while pidx > 0 and word[idx] != pattern[pidx]:
            pidx = table[pidx-1]

        if word[idx] == pattern[pidx]:
            if pidx == len(pattern) - 1:
                results.append(idx-len(pattern)+2)
                pidx = table[pidx]
            else:
                pidx += 1

    return results