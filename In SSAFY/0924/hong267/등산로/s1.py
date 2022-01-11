import sys

sys.stdin = open('input.txt')

def dfs(i, j, k, ans):
    global answer

    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]

        if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
            if mountain[i][j] > mountain[ni][nj]:
                visited[ni][nj] = True
                dfs(ni, nj, k, ans+1)
                visited[ni][nj] = False
            elif k and mountain[i][j] > mountain[ni][nj] - k:
                original = mountain[ni][nj]
                for cut in range(1, k+1):
                    mountain[ni][nj] = mountain[i][j] - cut
                    visited[ni][nj] = True
                    dfs(ni, nj, 0, ans+1)
                    mountain[ni][nj] = original
                    visited[ni][nj] = False

    if answer < ans:
        answer = ans


di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    mountain = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    answer = 0

    max_high = 0
    for i in range(N):
        for j in range(N):
            if mountain[i][j] > max_high:
                max_high = mountain[i][j]

    for i in range(N):
        for j in range(N):
            if mountain[i][j] == max_high:
                visited[i][j] = True
                dfs(i, j, K, 1)
                visited[i][j] = False

    print('#{} {}'.format(tc, answer))