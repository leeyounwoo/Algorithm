import sys
sys.stdin = open('input.txt')


def find_set(x):
    if parents[x] != x:
        parents[x] = find_set(parents[x])

    return parents[x]


def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)

    if ranks[root_x] > ranks[root_y]:
        parents[root_y] = root_x
    else:
        parents[root_x] = root_y
        if ranks[root_x] == ranks[root_y]:
            ranks[root_y] += 1


T = int(input())

answer = []
for tc in range(1, T + 1):

    N, M = map(int, input().split())

    parents = [i for i in range(N+1)]
    ranks = [0 for _ in range(N+1)]

    couple_requests = list(map(int, input().split()))

    for i in range(0, len(couple_requests), 2):
        u, v = couple_requests[i], couple_requests[i+1]
        union(u, v)

    for i in range(1, N+1):
        find_set(i)

    couple_set = set({})
    for i in range(1, N+1):
        couple_set.add(parents[i])
    result = len(couple_set)
    answer.append(result)

for tc in range(1, T + 1):
    print(f'#{tc} {answer[tc-1]}')
