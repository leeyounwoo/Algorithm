import sys
sys.stdin = open("input.txt")
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(N)]
    result = []
    max_num = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            total = 0
            for l in range(M):
                for m in range(M):
                    total += flies[i+l][j+m]
            if max_num < total:
                max_num = total
    print('#{} {}'.format(tc, max_num))
