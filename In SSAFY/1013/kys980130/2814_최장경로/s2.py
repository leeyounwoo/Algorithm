def dfs_recursive(v, cnt):
    global max_len
    if cnt > max_len:
        max_len = cnt

    for u in range(1, N+1):
        if adj_mat[v][u] and not visited[u]:
            visited[u] = 1
            dfs_recursive(u, cnt+1)
            visited[u] = 0
import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    adj_mat = [[0 for _ in range(N+1)] for _ in range(N+1)]
    visited = [0] * (N + 1)
    max_len = 0
    for _ in range(M):
        s, e = map(int, input().split())
        adj_mat[s][e] = 1
        adj_mat[e][s] = 1
    for i in range(1, N+1):
        visited[i] = 1
        dfs_recursive(i, 1)
        visited[i] = 0
    print('#{} {}'.format(tc, max_len))