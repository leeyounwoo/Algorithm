import sys
sys.stdin = open('input.txt')

T = int(input())

answer = []
for tc in range(1, T + 1):

    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for i in range(N):
        for j in range(N):
            for ki, kj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                if (0 <= i + ki < 5) and (0 <= j + kj < 5):
                    result += abs(arr[i][j] - arr[i + ki][j + kj])

    answer.append(result)

for tc in range(1, T + 1):
    print('#{0} {1}'.format(tc, answer[tc-1]))