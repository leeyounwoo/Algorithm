import sys
sys.stdin = open('input.txt')

for _ in range(10):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    visited = [[False for _ in range(16)] for _ in range(16)]
    dir_x = [0, 1, 0, -1]
    dir_y = [1, 0, -1, 0]
    start_x, start_y = 0, 0
    end_x, end_y = 0, 0

    # 출발 / 도착 위치 탐색
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                start_x, start_y = i, j
            if maze[i][j] == 3:
                end_x, end_y = i, j

    queue = []
    queue.append([start_x, start_y])
    visited[start_x][start_y] = True

    while queue:
        curr_x, curr_y = queue.pop(0)
        for i in range(4):
            next_x, next_y = curr_x + dir_x[i], curr_y + dir_y[i]
            if 0 <= next_x < 16 and 0 <= next_y < 16 and not visited[next_x][next_y] and not maze[next_x][next_y] == 1:
                visited[next_x][next_y] = True
                queue.append([next_x, next_y])

    ans = 1 if visited[end_x][end_y] else 0
    print('#{} {}'.format(tc, ans))
