import sys
sys.stdin = open('input.txt')


def dfs(v, cnt):
    global result

    result = max(result, cnt)

    for i in range(1, N+1):
        if mat[v][i] and not visited[i]:
            visited[i] = 1
            dfs(i, cnt+1)
            visited[i] = 0


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    mat = [[0 for _ in range(N+1)] for _ in range(N+1)]
    visited = [0] * (N + 1)
    for _ in range(M):
        x, y = map(int, input().split())
        mat[x][y] = 1
        mat[y][x] = 1

    result = 0
    for i in range(1, N+1):
        visited = [0] * (N + 1)
        visited[i] = 1
        dfs(i, 1)

    print('#{} {}'.format(tc, result))
