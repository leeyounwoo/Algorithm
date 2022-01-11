import sys
sys.stdin = open('input.txt')

T = int(input())
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


for tc in range(T):
    N = int(input())
    boxes = [[0] * N for _ in range(N)]
    x = y = 0
    dir_stat = 0
    for i in range(1, N**2 + 1):
        boxes[y][x] = i

        x += dx[dir_stat]
        y += dy[dir_stat]

        if x >= N or y >= N or boxes[y][x] != 0:
            x -= dx[dir_stat]
            y -= dy[dir_stat]
            dir_stat = (dir_stat+1) % 4

            x += dx[dir_stat]
            y += dy[dir_stat]

    print('#{}'.format(tc))
    for n in boxes:
        print(*n)
