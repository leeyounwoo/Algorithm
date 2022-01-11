import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    adj_mat = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    result = []
    for i in range(0, M):
        s, e = map(int, input().split())
        adj_mat[s][e] = 1
        adj_mat[e][s] = 1
    s = 1
    stack = [s]
    visited = [0] * (N + 1)

    while stack:
        v = stack.pop()

        if not visited[v]:

            visited[v] = 1
            result.append(v)

            for u in range(1, N + 1):
                if adj_mat[v][u] and not visited[u]:
                    stack.append(u)

    for j in result:
        if result.count(j) >= 2:
            result.remove(j)
    print('#{} {}'.format(tc, len(result)))

