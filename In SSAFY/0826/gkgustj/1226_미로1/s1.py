import sys
sys.stdin = open('input.txt')

def bfs(i, j):
    global result

    dxy = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    queue = [(i, j)]

    while queue:
        x, y = queue.pop(0)

        if maze[x][y] == 3:
            result = 1
            return

        for dx, dy in dxy:
            nx, ny = x+dx, y+dy

            if maze[nx][ny] in (0, 3):
                if maze[nx][ny] ==0:
                    maze[nx][ny] = 1 # 방문처리
                queue.append((nx, ny))


for _  in range(10):
    t = int(input())

    maze = []

    for _ in range(16):
        temp = []
        for s in input():
            temp.append(int(s))
        maze.append(temp)

    result = 0

    bfs(1, 1)

    print('#{} {}'.format(t, result))
