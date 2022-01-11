import sys
sys.stdin = open('input.txt')


def make_set(x):
    parents[x] = x
    ranks[x] = 0


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


def find_MST(edges):
    MST = []

    for edge in edges:
        x, y, w = edge
        if find_set(x) != find_set(y):
            MST.append((x, y, w))
            union(x, y)

    return MST


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]

    parents = [0] * (V + 1)
    ranks = [0] * (V + 1)

    for v in range(1, V+1):
        make_set(v)

    edges.sort(key=lambda x: x[2])
    result = 0
    for edge in find_MST(edges):
        result += edge[2]

    print('#{} {}'.format(tc, result))
