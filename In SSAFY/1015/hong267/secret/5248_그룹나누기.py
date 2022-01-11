"""
Thanks to 홍중
"""

import sys
sys.stdin = open('input.txt')

T = int(input())

def find_set(x):
    if x != parents[x]:
        parents[x] = find_set(parents[x])

    return parents[x]

for tc in range(1, T+1):
    N, M = map(int, input().split())
    temp = list(map(int, input().split()))
    papers = []
    for i in range(0, M*2, 2):
        papers.append([temp[i], temp[i+1]])

    parents = [0 for _ in range(N+1)]
    ranks = [0 for _ in range(N+1)]
    for i in range(1, N+1):
        parents[i] = i

        p1 = find_set(paper[0])
        p2 = find_set(paper[1])

        if ranks[p1] > ranks[p2]:
            parents[p2] = p1
        elif ranks[p1] == ranks[p2]:
            ranks[p2] += 1
            parents[p1] = p2
        else:
            parents[p1] = p2

    result = set()
    for i in range(1, len(parents)):
        result.add(find_set(parents[i]))

    print('#{0} {1}'.format(tc, len(result)))