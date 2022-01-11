import sys
sys.stdin = open('input.txt')

TC = int(input())
for tc in range(TC):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]

    dir_x = [0, 1, 0, -1]
    dir_y = [1, 0, -1, 0]

    start_x, start_y = 0, 0
    end_x, end_y = 0, 0

    # 출발 도착 정보 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start_x, start_y = i, j
            if maze[i][j] == 3:
                end_x, end_y = i, j

    queue = []
    queue.append([start_x, start_y])
    visited[start_x][start_y] = 1
    while queue:
        curr_x, curr_y = queue.pop(0)
        for i in range(4):
            next_x, next_y = curr_x + dir_x[i], curr_y + dir_y[i]
            if 0 <= next_x < N and 0 <= next_y < N and not visited[next_x][next_y] and not maze[next_x][next_y] == 1:
                visited[next_x][next_y] = visited[curr_x][curr_y] + 1
                queue.append([next_x, next_y])


    ans = visited[end_x][end_y] -2 if visited[end_x][end_y] else 0

    print('#{} {}'.format(tc+1, ans))
