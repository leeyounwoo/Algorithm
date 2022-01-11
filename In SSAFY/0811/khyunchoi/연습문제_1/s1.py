import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    result = 0
    for i in range(N):
        for j in range(N):
            near_sum = 0
            for k in range(4):
                if 0 <= i+dx[k] < N and 0 <= j+dy[k] < N:
                    near_sum += abs(arr[i][j] - arr[i+dx[k]][j+dy[k]])

            result += near_sum

    print('#{} {}'.format(tc, result))