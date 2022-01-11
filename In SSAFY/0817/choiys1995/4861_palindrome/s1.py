import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    result = []

    arr = []
    for _ in range(N):
        arr.append(input())

    for row in range(N):
        for col in range(N - M + 1):
            if arr[row][col : col + M] == arr[row][col : col + M][ : : -1]:
                result.append(arr[row][col : col + M])

    for row in range(N - M + 1):
        for col in range(N):
            col_list = []
            for i in range(M):
                col_list.append(arr[row + i][col])
            if col_list == col_list[ : : -1]:
                result.append(''.join(col_list))

    print('#{} {}'.format(tc, result[0]))