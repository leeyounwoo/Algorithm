def tour(y, x, dir, cnt):
    global result, sy, sx

    # 경로를 벗어나면 취소
    if (x > N - 1 or x < 0 or y > N - 1 or y < 0):
        return
    # 방문한 적이 있거나 먹은 적이 있는 디저트면 취소
    if visited[y][x] or desert[mat[y][x]]:
        return

    if y == sy and x == sx:
        if cnt > result:
            result = cnt
        return

    visited[y][x] = 1
    desert[mat[y][x]] = 1

    if dir == 1:
        tour(y + 1, x + 1, 1, cnt + 1)  # right down (dir-1)
        tour(y + 1, x - 1, 2, cnt + 1)  # left down (dir-2)
    elif dir == 2:
        tour(y + 1, x - 1, 2, cnt + 1)
        tour(y - 1, x - 1, 3, cnt + 1)  # left up (dir-3)
    elif dir == 3:
        tour(y - 1, x - 1, 3, cnt + 1)  # left up (dir-3)
        tour(y - 1, x + 1, 4, cnt + 1)  # right up (dir-4)
    elif dir == 4:
        tour(y - 1, x + 1, 4, cnt + 1)  # right up (dir-4)

    visited[y][x] = 0
    desert[mat[y][x]] = 0


T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]

    desert = [0] * 101
    visited = [[0 for _ in range(N)] for _ in range(N)]

    result = 0
    for y in range(N):
        for x in range(N):
            sy, sx = y, x
            tour(y + 1, x + 1, 1, 1)  # dir: 1, 2, 3, 4

    if result > 0:
        print(f'#{tc} {result}')
    else:
        print(f'#{tc} -1')
