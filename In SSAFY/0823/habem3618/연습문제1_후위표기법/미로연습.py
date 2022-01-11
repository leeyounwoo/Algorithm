'''
8
0 0 1 1 1 1 1 1
1 0 0 0 0 0 0 1
1 1 1 0 1 1 1 1
1 1 1 0 1 1 1 1
1 0 0 0 0 0 0 1
1 0 1 1 1 1 1 1
1 0 0 0 0 0 0 0
1 1 1 1 1 1 1 0
'''

def dfs(sy, sx):
    # 핵심 아이디어
    # 다음 지점으로 갈 때 "필요한 정보를 같이 가져가기"
    stack = [(sy, sx, [])]

    dyx = ((0, 1), (1, 0), (0, 1)) # 오른쪽, 아래, 위쪽 순서
    while stack:
        # 현재 방문할 위치
        y, x, path = stack.pop()
        maze[y][x] = 1  # 방문 체크

        # 현재 위치(y,x)에서 갈 수 있는 곳 탐색
        for dy, dx in dyx:
            ny, nx = y + dy, x + dx
            # 갈 수 있는지 판단
            # 1. 새로운 위치(ny, nx)가 배열의 범위를 벗어나지 않는지?
            # 2. 새로운 위치(ny, nx)가 벽이 아닌지?
            if 0 <= ny <= N-1 and 0 <= nx <= N-1:
                if maze[ny][nx] == 0:
                    # 종료지점에 도착하면 경로 반환
                    if ny == N-1 and nx == N-1:
                        return path

                    # 다음에 방문할 곳으로 스택에 추가
                    stack.append((ny, nx, path + [[y, x]]))



N = int(input())
maze = [list(map(int, input().split())) for _ in range(N)]
sy, sx = 0, 0
result = dfs(sy,sx)
print(result)