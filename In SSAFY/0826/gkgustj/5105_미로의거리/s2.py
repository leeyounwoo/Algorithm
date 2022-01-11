import sys
sys.stdin = open('input.txt')

def find_maze(i, j):
    global result

    cnt = [[0]*(N) for _ in range(N)]
    queue = [(i, j)]
    dxy = [(0, -1), (0, 1), (-1, 0), (1, 0)] #좌우상하

    while queue:
        x, y = queue.pop(0)
        maze[x][y] = 1

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            # 벽이 아니고 미로에서 0이거나 2일때
            if nx in range(N) and ny in range(N) and maze[nx][ny] in (0, 2):
                if maze[nx][ny] == 0:
                    queue.append((nx, ny))
                    cnt[nx][ny] = cnt[x][y] + 1

                if maze[nx][ny] == 2:
                    result = cnt[x][y]
                    return


T = int(input())

for t in range(1, T+1):
    N = int(input())

    maze = []
    for _ in range(N):
        temp = []
        for s in input():
            temp.append(int(s))
        maze.append(temp)

    # 도착지 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 3:
                break
        if maze[i][j] == 3:
            break

    result = 0
    find_maze(i, j)

    print('#{} {}'.format(t, result))