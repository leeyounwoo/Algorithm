import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    N = int(input())
    arr = [[0] * (N) for _ in range(N)]

    dx = [0, 1, 0, -1] # 우 하 좌 상
    dy = [1, 0, -1, 0]

    direction = 0 # 방향 초기설정
    x = y = 0
    num = 1

    while num <= N * N:
        arr[x][y] = num
        num += 1

        nx = x + dx[direction]
        ny = y + dy[direction]
        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 0:
            x, y = nx, ny
        else:
            direction = (direction+1)%4
            x += dx[direction]
            y += dy[direction]

    print("#{}".format(tc+1))
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end = " ")
        print()