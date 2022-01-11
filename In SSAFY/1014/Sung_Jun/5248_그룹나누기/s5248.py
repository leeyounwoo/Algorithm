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
        return False

    parents[root_y] = root_x
    return True

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    nodes = list(range(N+1))
    parents = [0] * (len(nodes) + 1)
    case = list(map(int, input().split()))

    for node in nodes:
        make_set(node)

    for i in range(M):
        union(case[i*2], case[i*2 + 1])

    result = []
    for num in range(1, N+1):
        if find_set(num) not in result:
            result.append(find_set(num))
    print(result)
    print('#{} {}'.format(tc+1, len(result)))
