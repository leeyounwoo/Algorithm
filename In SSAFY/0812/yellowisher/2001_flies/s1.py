import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max = 0
    for i in range(N + 1 - M):
        for j in range(N + 1 - M):
            sum_num = 0
            for x in range(i, i + M):
                for y in range(j, j + M):
                    sum_num += arr[x][y]
            if sum_num > max:
                max = sum_num

    print('#{} {}'.format(tc+1, max))