import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]

    cnt = 1
    i, j = 0, -1
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    k = 0
    while cnt <= N*N:
        x, y = i+dx[k], j+dy[k]
        if x < N and y < N and arr[x][y] == 0:
            arr[x][y] = cnt
            i, j = x, y
            cnt += 1
        else:
            k = (k+1) % 4

    print('#{}'.format(tc))
    for i in arr:
        print(*i)