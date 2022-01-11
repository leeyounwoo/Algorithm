import sys
sys.stdin = open('input.txt')

def bfs(sy, sx):
    queue = [(sy, sx, [])]
    dyx = ((0, 1), (-1, 0), (0, -1), (1, 0)) # 오른쪽, 위, 왼쪽, 아래 순서

    while queue:
        y, x, path = queue.pop(0)
        maze[y][x] = 1

        for dy, dx in dyx:
            ny, nx = y + dy, x + dx

            if 0 <= ny <= N-1 and 0 <= nx <= N-1:
                if maze[ny][nx] == 0:
                    queue.append((ny, nx, path + [[y, x]]))
                elif maze[ny][nx] == 3:
                    return len(path)

    return 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                sy, sx = i, j

    result = bfs(sy, sx)

    print('#{} {}'.format(tc, result))
