import sys
sys.stdin = open('input.txt')


def find_set(x):
    if x != parents[x]:
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

    parents = [i for i in range(N + 1)]
    ranks = [0 for _ in range(N + 1)]

    for _ in range(M):
        u, v = map(int, input().split())
        union(u, v)

    for i in range(1, N + 1):
        find_set(i)

    group_set = set()
    for i in range(1, N + 1):
        group_set.add(parents[i])

    result = len(group_set)

    answer.append(result)

for tc in range(1, T + 1):
    print(f'#{tc} {answer[tc-1]}')
