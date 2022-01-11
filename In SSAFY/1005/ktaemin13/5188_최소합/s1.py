import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    matrix = [list((map(int, input().split()))) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if i == j == 0:  # 시작점
                continue
            if i == 0 and j > 0:  # 첫 번째 column
                matrix[j][i] += matrix[j - 1][i]
            elif j == 0 and i > 0:  # 첫 번째 row
                matrix[j][i] += matrix[j][i - 1]
            elif i > 0 and j > 0:  # 최솟값 더해줌
                matrix[j][i] += min(matrix[j - 1][i], matrix[j][i - 1])

    print("#{} {}".format(test_case, matrix[N-1][N-1]))
