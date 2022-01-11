import sys
sys.stdin = open("input.txt")

def dfs(sy, sx):

    stack = [(sy, sx, [])]

    dyx = ((0, 1), (-1, 0), (0, -1), (1, 0))  # 오른쪽, 위, 왼쪽, 아래 순서
    while stack:
        y, x, path = stack.pop()
        maze[y][x] = 1

        for dy, dx in dyx:
            ny, nx = y + dy, x + dx

            if 0 <= ny <= 16 and 0 <= nx <= 16:
                if maze[ny][nx] == 0:
                    stack.append((ny, nx, path + [[y, x]]))
                elif maze[ny][nx] == 3:
                    return path


T = 10
for tc in range(1, 11):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(16)]

    for i in range(0, 16):
        for j in range(0, 16):
            if maze[j][i] == 2:
                sy, sx = j, i
    result = dfs(sy, sx)

    if result == None:
        print('#{} 0'.format(tc))
    else:
        print('#{} 1'.format(tc))
