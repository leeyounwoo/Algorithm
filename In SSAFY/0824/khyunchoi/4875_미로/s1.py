import sys
sys.stdin = open('input.txt')


def dfs(sy, sx):
    global is_find
    maze[sy][sx] = 1
    dyx = ((0, 1), (1, 0), (0, -1), (-1, 0)) # 오른쪽 아래 왼쪽 위

    for dy, dx in dyx:
        ny = sy + dy
        nx = sx + dx
        if 0 <= ny < N and 0 <= nx < N:
            if maze[ny][nx] == 3:
                is_find = True
                return
            elif maze[ny][nx] == 0:
                dfs(ny, nx)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    is_find = False

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                sy, sx = i, j

    dfs(sy, sx)

    result = 0
    if is_find:
        result = 1

    print('#{} {}'.format(tc, result))