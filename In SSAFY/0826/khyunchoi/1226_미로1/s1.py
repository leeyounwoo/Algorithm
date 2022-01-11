import sys
sys.stdin = open('input.txt')


def dfs(sy, sx):
    stack = []
    stack.append((sy, sx))
    dyx = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while stack:
        ty, tx = stack.pop()
        maze[ty][tx] = 1

        for dy, dx in dyx:
            ny = ty + dy
            nx = tx + dx
            if 0 <= ny < N and 0 <= nx < N:
                if maze[ny][nx] == 0:
                    stack.append((ny, nx))
                elif maze[ny][nx] == 3:
                    return 1
    return 0


T = 10
for tc in range(1, T+1):
    N = 16
    _ = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                sy, sx = i, j
                break

    result = dfs(sy, sx)
    print('#{} {}'.format(tc, result))