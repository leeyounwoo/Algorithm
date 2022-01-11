import sys
sys.stdin = open('input.txt')
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def work(y, x, road, skill):
    global ans
    if road > ans:
        ans = road

    visited[y][x] = 1

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
            if mountain[ny][nx] < mountain[y][x]:
                work(ny, nx, road+1, skill)
            elif skill and mountain[ny][nx] - K < mountain[y][x]:
                tmp = mountain[ny][nx]
                mountain[ny][nx] = mountain[y][x] - 1
                work(ny, nx, road+1, 0)
                mountain[ny][nx] = tmp

    visited[y][x] = 0

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    mountain = [list(map(int, input().split())) for _ in range(N)]
    max_height = 0
    for i in range(N):
        for j in range(N):
            if mountain[i][j] > max_height:
                max_height = mountain[i][j]

    visited = [[0] * N for _ in range(N)]
    ans = 0

    for i in range(N):
        for j in range(N):
            if mountain[i][j] == max_height:
                work(i, j, 1, 1)
    print('#{} {}'.format(tc, ans))
