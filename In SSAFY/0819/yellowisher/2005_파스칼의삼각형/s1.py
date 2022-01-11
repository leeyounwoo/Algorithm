import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    N = int(input())
    print("#{}".format(tc + 1))

    arr = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(i + 1):
            if j == 0 or i == j: # 첫째 자리와 마지막 자리는 무조건 1
                arr[i][j] = 1
            else:
                arr[i][j] = arr[i-1][j] + arr[i-1][j-1] # 첫째와 마지막이 아닌 경우 위쪽과 왼쪽 대각선 값을 더해줌

        for k in range(i + 1):
            print(arr[i][k], end = " ")
        print()

