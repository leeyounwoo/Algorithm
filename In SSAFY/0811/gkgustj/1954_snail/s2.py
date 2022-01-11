import sys

sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    N = int(input())

    result = [[0]*N for _ in range(N)]

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    x = 0
    y = 0
    way = 0

    for n in range(1, N**2+1):
        result[x][y] = n
        x_ = x + dx[way]
        y_ = y + dy[way]

        if x_ not in range(N) or y_ not in range(N) or result[x_][y_] != 0:
            way = (way + 1) % 4

        x += dx[way]
        y += dy[way]

    print(f'#{t}')
    for row in result:
        print(*row)