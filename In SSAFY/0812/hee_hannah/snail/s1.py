import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [[0 for _ in range(N)] for _ in range(N)]

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    dir_stat = 0

    x = 0
    y = 0
    for i in range(1, N*N + 1):
        new_x = x + dx[dir_stat]
        new_y = y + dy[dir_stat]

        if (new_x > N -1 or new_x < 0 or new_y > N - 1 or new_y < 0 or arr[new_y][new_x] != 0):
            dir_stat = (dir_stat + 1) % 4
            new_x = x + dx[dir_stat]
            new_y = y + dy[dir_stat]

        arr[y][x] = i

    print("#{}".format(tc))
    for i in range()
        print(*i)


