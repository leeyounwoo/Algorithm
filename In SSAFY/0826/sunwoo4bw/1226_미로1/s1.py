import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, 10):
    N = input()
    maze = [list(map(int, input())) for _ in range(16)]
    visited = [[False for _ in range(16)] for _ in range(16)]
    dir_x = [0, 1, 0, -1] # 상 우 하 좌
    dir_y = [1, 0 -1, 0]
    result = 0

    # 시작 위치 탐색
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                s_x, s_y = i, j

    queue = [[s_x, s_y]]
    visited[s_x][s_y] = True

    while queue:
        curr_x, curr_y = queue.pop(0)
        if maze[curr_x][curr_y] == 3:
            result = 1
        maze[curr_x][curr_y] = 1
# ing

