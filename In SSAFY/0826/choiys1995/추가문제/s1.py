import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] in 'ABC':
                if arr[i][j] == 'A':
                    n = 1
                elif arr[i][j] == 'B':
                    n = 2
                else:
                    n = 3
                for k in range(1, 1 + n):
                    if -1 < i + k < N and arr[i + k][j] == 'H':  # 남
                        arr[i + k][j] = 'X'
                    if -1 < i - k < N and arr[i - k][j] == 'H':  # 북
                        arr[i - k][j] = 'X'
                    if -1 < j + k < N and arr[i][j + k] == 'H':  # 동
                        arr[i][j + k] = 'X'
                    if -1 < j - k < N and arr[i][j - k] == 'H':  # 서
                        arr[i][j - k] = 'X'

    cnt = 0
    for i in range(N):
        cnt += arr[i].count('H')

    print('#{} {}'.format(tc, cnt))

