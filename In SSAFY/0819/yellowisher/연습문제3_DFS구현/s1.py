import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    N = int(input())
    print("#{}".format(tc + 1))

    arr = [[0] * N for _ in range(N)]
    arr[0][0] = 1
    for i in range(N):
        for j in range(i + 1):
            if j == 0 or i == j:
                arr[i][j] = 1
            else:
                arr[i][j] = arr[i-1][j] + arr[i-1][j-1]

        for k in range(i + 1):
            print(arr[i][k], end = " ")
        print()

