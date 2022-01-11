import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    home = [list(map(str, input())) for _ in range(N)]

    dyx_1 = ((0, 1), (-1, 0), (0, -1), (1, 0))
    dyx_2 = ((0, 2), (-2, 0), (0, -2), (2, 0))
    dyx_3 = ((0, 3), (-3, 0), (0, -3), (3, 0))

    for i in range(N):
        for j in range(N):

            if home[i][j] == 'A':
                for dy, dx in dyx_1:
                    ny, nx = i + dy, j + dx
                    if home[ny][nx] == "H":
                        home[ny][nx] = "X"

            elif home[i][j] == 'B':
                for dy, dx in dyx_2:
                    ny, nx = i + dy, j + dx
                    if home[ny][nx] == "H":
                        home[ny][nx] = "X"

            elif home[i][j] == 'C':
                for dy, dx in dyx_3:
                    ny, nx = i + dy, j + dx
                    if home[ny][nx] == "H":
                        home[ny][nx] = "X"

    count = 0
    for i in range(N):
        for j in range(N):
            if home[i][j] == "H":
                count += 1

    print('#{} {}'.format(tc, count))


