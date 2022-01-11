import sys
sys.stdin = open('input.txt')

def dfs(sy, sx):
    stack = [(sy, sx)]

    dyx = ((0, 1), (-1, 0), (1, 0), (0, -1)) # 오른쪽, 아래, 왼쪽, 위쪽 순서
    while stack:
        # 현재 방문할 위치
        y, x = stack.pop()
        # maze[y][x] = '1'  # 방문체크
        for dy, dx in dyx:
            ny, nx = y + dy, x + dx

            if 0 <= ny < 16 and 0 <= nx < 16:
                if maze[ny][nx] == '0':
                    # 종료지점에 도착하면 경로 반환
                    stack.append((ny, nx))
                    maze[ny][nx] = '1'  # 방문체크
                if maze[ny][nx] == '3':
                    return 1
    return 0

T = 10

for _ in range(1, T+1):
    tc = int(input())
    maze = [list(input()) for _ in range(16)]
    sy, sx = 0, 0
    for i in range(16):
        for j in range(16):
            if maze[i][j] == '2':
                sy, sx = i, j
    print('#{} {}'.format(tc, dfs(sy, sx)))