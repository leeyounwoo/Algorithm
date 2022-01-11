def dfs(sy, sx):
    stack = [(sy, sx, [])]

    dyx = ((0, 1), (1, 0), (0, -1)) # 오른쪽, 아래, 왼쪽 순서
    while stack:
        y, x, path = stack.pop()
        maze[y][x] = 1

        for dy, dx in dyx:
            ny, nx = y + dy, x + dx
            if 0 <= ny <= N-1 and 0 <= nx <= N-1:
                if maze[ny][nx] == 0:
                    if ny == N-1 and nx == N-1:
                        return path

                    stack.append((ny, nx, path + [[y, x]]))


N = int(input())
maze = [list(map(int, input().split())) for _ in range(N)]
sy, sx = 0, 0

result = dfs(sy, sx)
print(result)