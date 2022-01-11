import sys
sys.stdin = open('input.txt')

# 1 가능 0 불가능 (도착여부)
# 0 통로 1 벽 2 출발점 3 도착점

dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def maze_start(maze):
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                x, y = i, j
    return x, y

def maze_runner(x, y, visited):
    stack = []
    stack.append((x, y))

    while stack:
        x, y = stack.pop()
        if visited[x][y] == 0:
            visited[x][y] = 1

        for i in dxy:
            nx = x + i[0]
            ny = y + i[1]

            if 0 <= nx < 16 and 0 <= ny < 16 and visited[nx][ny] == 0:
                if maze[nx][ny] == 0:
                    stack.append((nx, ny))
                    visited[nx][ny] = 1

                if maze[nx][ny] == 3:
                    visited[nx][ny] = 3
                    return 1

    return 0

for tc in range(1, 11):
    t = int(input())
    maze = [list(map(int, input())) for _ in range(16)]

    x, y  = maze_start(maze)
    visited = [[0] * 16 for _ in range(16)]
    answer = maze_runner(x, y, visited)

    print('#{} {}'.format(tc, answer))

