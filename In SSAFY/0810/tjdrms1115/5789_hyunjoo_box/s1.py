import sys
sys.stdin = open('input.txt')

T = int(input())

answer = []
for tc in range(1, T + 1):

    N, Q = map(int, input().split())

    LR = []
    for _ in range(Q):
        L, R = map(int, input().split())
        LR.append([L - 1, R - 1])

    colored = [0] * N

    for i in range(Q):
        L, R = map(int, LR[i])
        for j in range(L, R + 1):
            colored[j] = i + 1

    result = ' '.join(map(str, colored))
    answer.append(result)

for tc in range(1, T+1):
    print('#{0} {1}'.format(tc, answer[tc-1]))