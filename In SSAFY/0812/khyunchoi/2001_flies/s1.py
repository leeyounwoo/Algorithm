import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(N)]

    max_total = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            total = 0
            for x in range(i, i+M):
                for y in range(j, j+M):
                    total += flies[x][y]

            if max_total < total:
                max_total = total

    print('#{} {}'.format(tc, max_total))