def dfs(sy, sx):
    # 핵심 아이디어
    # 다음 지점으로 갈 때 "필요한 정보를 같이 가져가기"
    stack = [(sy, sx)]

    dyx = ((0, 1), (1, 0), (0, -1)) # 오른쪽, 아래, 왼쪽 순서
    while stack:
        y, x, path = stack.pop()
        arr[y][x] = 1 # 방문 체크

        for dy, dx in dyx:
            ny, nx = y + dy, x + dx
            # 갈 수 있는지 판단
            # 1. 새로운 위치(ny, nx)가 배열의 범위를 벗어나지 않는지?
            # 2. 새로운 위치(ny, nx)가 벽이 아닌지?
            if 0 <= ny <= n-1 and 0 <= nx <= n-1:
                if arr[ny][nx] == 0:
                    # 종료지점에 도착하면 경로 반환
                    if ny == n-1 and nx == n-1:
                        return path

                    # 다음에 방문할 곳으로 스택에 추가가
                    stack.append( (ny, nx, path + [[y, x]]))


n = int(input())
arr = [list(map(int(input().split()))) for _ in range(n)]
sy, sx = 0
print(dfs(0, 0))