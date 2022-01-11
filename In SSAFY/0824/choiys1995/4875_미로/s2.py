import sys
sys.stdin = open('input.txt')

def dfs(sy, sx):
    stack = [(sy, sx)]

    dyx = ((0, 1), (-1, 0), (1, 0), (0, -1)) # 오른쪽, 아래, 왼쪽 순서
    while stack:
        # 현재 방문할 위치
        y, x = stack.pop()
        maze[y][x] = 1 # 방문 체크

        for dy, dx in dyx:
            ny, nx = y + dy, x + dx

            if 0 <= ny <= N-1 and 0 <= nx <= N-1:
                if maze[ny][nx] == 0:
                    # 종료지점에 도착하면 경로 반환
                    stack.append((ny, nx))
                if maze[ny][nx] == 3:
                    return 1
    return 0
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, str(input()))) for _ in range(N)]
    for i in range(N):
        if 2 in maze[i]:
            sy = maze[i].index(2)
    sx = 0
    print('#{} {}'.format(tc, dfs(sy, sx)))