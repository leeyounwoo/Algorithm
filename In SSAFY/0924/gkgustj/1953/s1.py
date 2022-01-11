import sys
sys.stdin = open('input.txt')

def move(num):
    if num == 1:
        # 상하좌우
        dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    elif num == 2:
        dxy = [(-1, 0), (1, 0)]
    elif num == 3:
        dxy = [(0, -1), (0, 1)]
    elif num == 4:
        dxy = [(-1, 0), (0, 1)]
    elif num == 5:
        dxy = [(1, 0), (0, 1)]
    elif num == 6:
        dxy = [(1, 0), (0, -1)]
    elif num == 7:
        dxy = [(-1, 0), (0, -1)]

    return dxy


def bfs(i, j):
    queue = [(i, j)]

    visited = [[0 for _ in range(M)] for _ in range(N)]
    visited[i][j] = 1

    while queue:
        x, y = queue.pop(0)
        if visited[x][y] == L:
            break

        for dx, dy in move(tunnel[x][y]):
            nx, ny = x+dx, y+dy

            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and tunnel[nx][ny]:
                # 연결이 되어있는지 한 번 더 확인
                for tx, ty in move(tunnel[nx][ny]):
                    tempx, tempy = nx+tx, ny+ty
                    if tempx == x and tempy == y:
                        visited[nx][ny] = visited[x][y] + 1
                        queue.append((nx, ny))
    
    return visited


T = int(input())

for t in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    tunnel = [list(map(int, input().split())) for _ in range(N)]

    temp = bfs(R, C)
    cnt = 0
    for i in range(N):
        for j in range(M):
            if temp[i][j]:
                cnt += 1

    print('#{} {}'.format(t, cnt))