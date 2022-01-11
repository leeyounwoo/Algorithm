import sys
sys.stdin = open('input.txt')


def dfs(idx, cnt):
    global result
    visited[idx] = 1
    cnt += 1
    if result < cnt:
        result = cnt
    for i in adjL[idx]:
        if not visited[i]:
            dfs(i, cnt)
    visited[idx] = 0


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    visited = [0] * (N + 1)

    adjL = [[] for _ in range(N+1)]
    for i in range(M):
        s, e = map(int, input().split())
        adjL[s].append(e)
        adjL[e].append(s)
    print(adjL)
    result = 0
    for i in range(N):
        dfs(i, 0)

    print('#{} {}'.format(tc, result))


