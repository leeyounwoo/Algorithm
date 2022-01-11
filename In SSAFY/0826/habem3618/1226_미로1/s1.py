import sys
sys.stdin = open('input.txt')

def bfs(sy, sx):
    queue = [(sy, sx)]
    dyx = ((0, 1), (1, 0), (0, -1), (-1, 0)) # 오른쪽, 아래, 왼쪽  위쪽 순서

    while queue:
        # 현재 방문할 위치
        y, x = queue.pop(0)
        maze[y][x] = 1  # 방문 체크

        # 현재 위치(y,x)에서 갈 수 있는 곳 탐색
        for dy, dx in dyx:
            ny, nx = y + dy, x + dx

            if 0 <= ny <= 15 and 0 <= nx <= 15:
                if maze[ny][nx] == 0:
                    queue.append((ny, nx))
                if maze[ny][nx] == 3:
                    return 1
    return 0


for tc in range(1, 11):
    t = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    # 시작점 2의 위치 찾기
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                sy, sx = i, j

    print('#{} {}'.format(tc, bfs(sy, sx)))

