import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = []

    for i in range(N):
        arr.append(list(map(int, input().split())))
    result1 = list([0] * N for _ in range(N))
    result2 = list([0] * N for _ in range(N))
    result3 = list([0] * N for _ in range(N))

    # 90
    for i in range(N):
        for j in range(N):
            result1[j][i] = arr[N - i - 1][j]
    # 180
    for i in range(N):
        for j in range(N):
            result2[j][i] = result1[N - i - 1][j]
    # 270
    for i in range(N):
        for j in range(N):
            result3[j][i] = result2[N - i - 1][j]

    print('#{}'.format(tc))
    for i in range(N):
        for j in range(N):
            print(result1[i][j], end='')
        print(end=' ')
        for j in range(N):
            print(result2[i][j], end='')
        print(end=' ')
        for j in range(N):
            print(result3[i][j], end='')
        print()
