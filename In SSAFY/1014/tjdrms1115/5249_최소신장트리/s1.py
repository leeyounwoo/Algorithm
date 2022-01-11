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


def kruskal(V, edges):
    edges.sort(key=lambda x: x[2])
    count = 0
    idx = 0
    min_path = 0
    while count < V - 1:
        i, j, weight = edges[idx]
        i_root = find_set(i)
        j_root = find_set(j)
        if i_root != j_root:
            union(i_root, j_root)
            min_path += weight
            count += 1
        idx += 1
    return min_path


T = int(input())

answer = []
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    V += 1

    edges = [list(map(int, input().split())) for _ in range(E)]

    parents = [i for i in range(V)]
    ranks = [0 for _ in range(V)]

    result = kruskal(V, edges)

    answer.append(result)

for tc in range(1, T + 1):
    print(f'#{tc} {answer[tc-1]}')
