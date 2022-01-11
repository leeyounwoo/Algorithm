import sys
sys.stdin = open('input.txt')


def dfs(s, cnt):
    global ans
    if cnt > ans:
        ans = cnt

    for i in adj[s]:
        if not visited[i]:
            visited[i] = 1
            dfs(i, cnt+1)
            visited[i] = 0


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    visited = [0] * (N + 1)
    adj = {x: [] for x in range(1, N+1)}
    ans = 0

    for _ in range(M):
        x, y = map(int, input().split())
        adj[x].append(y)
        adj[y].append(x)

    for i in range(1, N+1):
        visited[i] = 1
        dfs(i, 1)
        visited[i] = 0

    print('#{} {}'.format(tc, ans))
