import sys
sys.stdin = open('input.txt')

def bfs(sy, sx, ey, ex):
    dyx = ((0, 1), (0, -1), (1, 0), (-1, 0))
    queue = [(sy, sx)]

    while queue:
        sy, sx = queue.pop(0)
        maze[sy][sx] = 1  # 방문 체크
        # 현재 위치(y, x)에서 갈 수 있는 곳 탐색
        for dy, dx in dyx:
            ny, nx = sy + dy, sx + dx

            if 0 <= ny <= N-1 and 0 <= nx <= N-1:
                if maze[ny][nx] == 0:
                    # 종료지점에 도착하면 경로 반환
                    queue.append((ny, nx))
                    # 거리 설정
                    distance[ny][nx] = distance[sy][sx] + 1
                if maze[ny][nx] == 3:
                    distance[ny][nx] = distance[sy][sx]

    # 실패하면 0, 성공하면 이동거리 출력
    return distance[ey][ex]


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    distance = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                sy, sx = i, j
            elif maze[i][j] == 3:
                ey, ex = i, j

    print('#{} {}'.format(tc, bfs(sy, sx, ey, ex)))