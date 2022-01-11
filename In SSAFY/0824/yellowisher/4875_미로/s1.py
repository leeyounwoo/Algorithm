import sys
sys.stdin = open('input.txt')

def dfs(sx, sy):
    global result
    maze[sx][sy] = 1  # 방문 처리
    dxy = ((-1, 0), (0, 1), (1, 0), (0, -1))  # 위, 오른쪽, 아래, 왼쪽

    for dx, dy in dxy:
        nx, ny = sx + dx, sy + dy
        if 0 <= nx <= N - 1 and 0 <= ny <= N - 1:
            if maze[nx][ny] == 0:
                dfs(nx, ny)

            if maze[nx][ny] == 3:
                result = 1
                return

T = int(input())
for tc in range(T):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    result = 0

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                x = i
                y = j

    dfs(x, y)
    print("#{} {}".format(tc + 1, result))

