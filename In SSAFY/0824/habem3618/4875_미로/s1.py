import sys
sys.stdin = open('input.txt')

def dfs(sy, sx):
    stack = [(sy, sx)]
    dyx = ((0, 1), (1, 0), (0, -1), (-1, 0)) # 오른쪽, 아래, 왼쪽  위쪽 순서

    while stack:
        # 현재 방문할 위치
        y, x = stack.pop()
        maze[y][x] = 1  # 방문 체크

        # 현재 위치(y,x)에서 갈 수 있는 곳 탐색
        for dy, dx in dyx:
            ny, nx = y + dy, x + dx

            if 0 <= ny <= N-1 and 0 <= nx <= N-1:
                if maze[ny][nx] == 0:
                    stack.append((ny, nx))
                if maze[ny][nx] == 3:
                    return 1
    return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    # 시작점 2의 위치 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                sy, sx = i, j

    print('#{} {}'.format(tc, dfs(sy, sx)))

