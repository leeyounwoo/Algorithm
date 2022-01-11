def dfs(sy, sx, path):
    case_box[sy][sx] = 1
    dyx = ((0, 1), (1, 0), (0, -1))

    for dy, dx in dyx:
        ny, nx = sy + dy, sx + dx
        if 0<= ny <= N-1 and 0 <= nx <= N-1:
            if case_box[ny][nx] == 0:
                if ny == N-1 and nx == N-1:
                    print(path)
                    return
                dfs(ny, nx, path + [[ny, nx]])


N = int(input())
case_box = [list(map(int, input().split())) for _ in range(N)]
sy, sx = 0, 0

print(dfs(sy, sx, []))