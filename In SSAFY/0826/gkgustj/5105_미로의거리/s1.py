import sys
sys.stdin = open('input.txt')

def find_maze(i, j):
    global result

    cnt = [[0]*(N) for _ in range(N)]
    queue = [(i, j)]
    dxy = [(0, -1), (0, 1), (-1, 0), (1, 0)] #좌우상하

    while queue:
        x, y = queue.pop(0)

        for dx, dy in dxy:
            nx, ny = x+dx, y+dy

            # 벽이 아니고 미로에서 0이거나 2일때
            if nx in range(N) and ny in range(N) and maze[nx][ny] in (0, 2):
                if maze[nx][ny] == 2:
                    result = cnt[x][y]
                    return

                maze[nx][ny] = 1  # 방문체크
                queue.append((nx, ny))

                # cnt에 이미 값이 있다면, 지금 바꾸려는 값이 원래 값보다 작은 경우에만 변경
                if cnt[nx][ny] and cnt[nx][ny] > cnt[x][y] + 1:
                    cnt[nx][ny] = cnt[x][y] + 1
                # cnt가 비어 있다면 바로 입력
                elif not cnt[nx][ny]:
                    cnt[nx][ny] = cnt[x][y] + 1


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