def dfs(sy, sx, path):
    maze[sy][sx] = 1
    dyx = ((0, 1), (1, 0), (0, -1))

    for dy, dx in dyx:
        ny, nx = sy + dy, sx + dx
        # 갈 수 있는 위치인지 판별
        if 0 <= ny <= N - 1 and 0 <= nx <= N - 1:
            if maze[ny][nx] == 0:
                if ny == N - 1 and nx == N - 1:
                    print(path)
                    return
                dfs(ny, nx, path + [[ny, nx]])

N = int(input())
maze = [list(map(int, input().split())) for _ in range(N)]
sy, sx = 0, 0
print(dfs(sy, sx, []))

# 8
# 0 0 1 1 1 1 1 1
# 1 0 0 0 0 0 0 1
# 1 1 1 0 1 1 1 1
# 1 1 1 0 1 1 1 1
# 1 0 0 0 0 0 0 1
# 1 0 1 1 1 1 1 1
# 1 0 0 0 0 0 0 0
# 1 1 1 1 1 1 1 0