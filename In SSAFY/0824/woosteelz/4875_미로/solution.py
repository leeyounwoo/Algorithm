import sys
sys.stdin = open('input.txt')

TC = int(input())

for tc in range(TC):
    maze_len = int(input())
    maze = [list(input()) for _ in range(maze_len)]
    ans = 0

    dir_x = [0, -1, 0, 1]
    dir_y = [1, 0, -1, 0]

    stack = []
    # 시작위치 탐색
    for i in range(maze_len):
        for j in range(maze_len):
            if maze[i][j] == '2':
                stack.append([i, j])

    while stack:
        curr_x, curr_y = stack.pop()

        if maze[curr_x][curr_y] == '3':
            ans = 1

        maze[curr_x][curr_y] = '1'

        for i in range(4):
            next_x, next_y = curr_x + dir_x[i], curr_y + dir_y[i]
            if 0 <= next_x < maze_len and 0 <= next_y < maze_len and not maze[next_x][next_y] == '1':
                stack.append([next_x, next_y])

    print('#{} {}'.format(tc+1, ans))
