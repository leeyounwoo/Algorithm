def make_set(x):
    parents[x] = x

def find_set(x):
    if x == parents[x]:
        return x

    return find_set(parents[x])

def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)

    if root_x == root_y:
        return False

    parents[root_y] = root_x
    return True

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    edges = list(map(int, input().split()))
    nodes = list(range(1, N+1))
    parents = [0] * (len(nodes) + 1)
    result = []
    for node in nodes:
        make_set(node)
    for i in range(0, len(edges) - 1, 2):
        x, y = edges[i], edges[i + 1]
        union(x, y)
    for j in range(1, N+1):
        if find_set(j) not in result:
            result.append(find_set(j))
    print('#{} {}'.format(tc, len(result)))