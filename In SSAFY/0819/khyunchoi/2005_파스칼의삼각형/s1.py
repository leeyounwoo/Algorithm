import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    arr = [[0]*N for _ in range(N)]
    for i in range(N):
        arr[i][0] = 1

    for i in range(1, N):
        for j in range(1, N):
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

    print('#{}'.format(tc))
    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                print(arr[i][j], end=' ')
        print()
