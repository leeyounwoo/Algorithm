import sys
sys.stdin = open('input.txt')


def dfs(idx, height):
    global result
    if result == B:
        return

    if B <= height:
        result = min(result, height)
        return

    for i in range(idx, N):
        if not visited[i]:
            visited[i] = 1
            dfs(i, height + peoples[i])
            visited[i] = 0


T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    peoples = list(map(int, input().split()))
    visited = [0] * N

    result = float('inf')
    dfs(0, 0)

    print('#{} {}'.format(tc, result - B))