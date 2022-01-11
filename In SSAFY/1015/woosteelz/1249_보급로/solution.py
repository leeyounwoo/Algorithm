from collections import deque


def solve(sy, sx):
    dyx = ((1, 0), (-1, 0), (0, 1), (0, -1))

    queue = deque()
    queue.append((sy, sx))
    distance[sy][sx] = 0

    while queue:
        y, x = queue.popleft()

        for dy, dx in dyx:
            ny, nx = y + dy, x + dx
            if (nx < 0 or nx > N - 1 or ny < 0 or ny > N - 1):
                continue

            if distance[y][x] + mat[ny][nx] < distance[ny][nx]:
                distance[ny][nx] = distance[y][x] + mat[ny][nx]
                queue.append((ny, nx))

    return distance[N-1][N-1]


for tc in range(int(input())):
    N = int(input())
    mat = [list(map(int, input())) for _ in range(N)]

    distance = [[float('inf') for _ in range(N)] for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]

    print(f'{tc+1} {solve(0, 0)}')
