import sys

sys.stdin = open('input.txt')

def find_set(x):
    if x == parents[x]:
        return x
    return find_set(parents[x])


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    relations = [list(map(int, input().split())) for _ in range(M)]

    ranks = [0 for _ in range(N+1)]
    parents = [0 for _ in range(N+1)]
    for i in range(1, N+1):
        parents[i] = i

    for r in relations:
        temp1 = find_set(r[0])
        temp2 = find_set(r[1])

        if temp1 != temp2:
            if ranks[temp1] > ranks[temp2]:
                parents[temp2] = temp1
            else:
                parents[temp1] = temp2

    result = set()
    for i in range(1, N+1):
        result.add(parents[find_set(i)])

    print('#{0} {1}'.format(tc, len(result)))