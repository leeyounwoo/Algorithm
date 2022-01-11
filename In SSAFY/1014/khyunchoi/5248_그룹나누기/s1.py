import sys
sys.stdin = open('input.txt')


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
        return

    parents[root_y] = root_x
    return


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    nodes = list(range(1, N+1))
    parents = [0] * (N + 1)
    tmp = list(map(int, input().split()))

    for node in nodes:
        make_set(node)

    for i in range(0, len(tmp), 2):
        a, b = tmp[i], tmp[i+1]
        union(a, b)

    result = set()
    for i in range(1, N+1):
        result.add(find_set(i))

    print('#{} {}'.format(tc, len(result)))
