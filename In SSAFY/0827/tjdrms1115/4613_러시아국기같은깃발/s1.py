import sys
sys.stdin = open('input.txt')

T = int(input())

answer = []
for tc in range(1, T+1):
    N, M = map(int, input().split())
    flag = [list(input()) for _ in range(N)]

    min_painting = 10000000
    for p1 in range(1, N-1):
        for p2 in range(p1+1, N):
            cur_painting = 0
            for i in range(0, p1):
                for j in range(M):
                    if flag[i][j] != 'W':
                        cur_painting += 1
            for i in range(p1, p2):
                for j in range(M):
                    if flag[i][j] != 'B':
                        cur_painting += 1
            for i in range(p2, N):
                for j in range(M):
                    if flag[i][j] != 'R':
                        cur_painting += 1
            if min_painting > cur_painting:
                min_painting = cur_painting

    result = min_painting
    answer.append(result)

for tc in range(1, T+1):
    print('#{} {}'.format(tc, answer[tc-1]))
