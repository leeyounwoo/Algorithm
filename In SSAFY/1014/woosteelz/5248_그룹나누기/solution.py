import sys
sys.stdin = open('1014/woosteelz/5248_그룹나누기/sample_input.txt')


def union(x, y):
    x = find_set(x)
    y = find_set(y)
    if rank[x] >= rank[y]:
        parent[y] = x
    else:
        parent[x] = y
    if rank[x] == rank[y]:
        rank[x] += 1


def find_set(x):
    if parent[x] == x:
        return x
    else:
        return find_set(parent[x])


for tc in range(int(input())):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    parent = [i for i in range(N + 1)]
    rank = [0] * (N + 1)
    for i in range(M):
        union(data[2 * i], data[2 * i + 1])
    groups = set()
    for i in range(1, 1 + N):
        groups.add(find_set(i))
    print('#{} {}'.format(tc + 1, len(groups)))
