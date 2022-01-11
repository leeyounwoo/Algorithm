from collections import deque

def solve(sy, sx):
    dyx = ((1, 0), (-1, 0), (0, 1), (0, -1))

    Q = deque()
    Q.append((sy, sx))
    distance[sy][sx] = 0

    while Q:
        y, x = Q.popleft()

        for dy, dx in dyx:
            ny, nx = y + dy, x + dx
            if (nx < 0 or nx > N - 1 or ny < 0 or ny > N - 1): continue

            # 다익스트라 아이디어 적용
            # S => X => G (S => X + X => G)
            if distance[y][x] + mat[ny][nx] < distance[ny][nx]:
                distance[ny][nx] = distance[y][x] + mat[ny][nx]
                Q.append((ny, nx))

    return distance[N-1][N-1]

t = int(input())
for tc in range(1, 1+t):
    N = int(input())
    mat = [list(map(int, input())) for _ in range(N)]

    distance = [[float('inf') for _ in range(N)] for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
