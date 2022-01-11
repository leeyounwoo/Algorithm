def dfs(sy, sx, path):
    arr[sy][sx] = 1 # 방문 처리
    dyx = ((0, 1), (1, 0), (0, -1))

    for dy, dx in dyx:
        ny, nx = sy+dy, sx+dx
        # 갈 수 있는 위치인지 판별
        if 0 <= ny <= n-1 and 0 <= nx <= n-1:
            if arr[ny][nx] == 0:
                # 만약에 종료 지점에 다다르면
                if ny == n-1 and nx == n-1:
                    print(path)
                    return

                dfs(ny, nx, path + [ [ny, nx] ])


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
sy, sx = 0, 0

result = dfs(sy, sx, [])
print(result)