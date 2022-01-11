import sys
sys.stdin = open('input.txt')

def find_maze(x, y):
    global result

    if maze[x][y] == 3:
        result = 1
        return

    maze[x][y] = 1

    # 좌 우 상 하
    dxy = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    for dx, dy in dxy:
        nx, ny = x + dx, y + dy

        if nx in range(N) and ny in range(N) and maze[nx][ny] in (0, 3):
            find_maze(nx, ny)


T = int(input())

for t in range(1, T+1):
    N = int(input())
    maze = []
    for _ in range(N):
        temp = []
        for num in input():
            temp.append(int(num))

        maze.append(temp)

    # 출구 좌표
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                break
        if maze[i][j] == 2:
            break

    result = 0
    find_maze(i, j)
    print('#{} {}'.format(t, result))