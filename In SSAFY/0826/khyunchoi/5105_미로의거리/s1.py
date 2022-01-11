import sys
sys.stdin = open('input.txt')


def bfs(sy, sx):
    global result
    queue = []
    queue.append((sy, sx))
    maze[sy][sx] = 1
    dyx = ((0, 1), (1, 0), (0, -1), (-1, 0)) # 오른쪽 아래 왼쪽 위

    while queue:
        ty, tx = queue.pop(0)

        for dy, dx in dyx:
            ny = ty + dy
            nx = tx + dx
            if 0 <= ny < N and 0 <= nx < N:
                if maze[ny][nx] == 3:
                    result = distance[ty][tx]
                elif maze[ny][nx] == 0:
                    queue.append((ny, nx))
                    maze[ny][nx] = 1
                    distance[ny][nx] = distance[ty][tx] + 1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    distance = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                sy, sx = i, j

    result = 0
    bfs(sy, sx)

    print('#{} {}'.format(tc, result))