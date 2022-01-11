import sys
sys.stdin = open('input.txt')
from pprint import pprint

for T in range(1, 1+int(input())):
    N, M = map(int, input().split())
    checkboard = [[0] * (N+1) for _ in range(N+1)]
    middle = N // 2
    checkboard[middle][middle] = 2
    checkboard[middle+1][middle] = 1
    checkboard[middle+1][middle+1] = 2
    checkboard[middle][middle+1] = 1
    for _ in range(M):
        now_j, now_i, c = map(int, input().split())
        checkboard[now_i][now_j] = c
        if c == 1:
            for j in range(N+1):
                # 가로
                if checkboard[now_i][j] == 2:
                    checkboard[now_i][j] = c
                # 세로
                if checkboard[j][now_j] == 2:
                    checkboard[j][now_j] = c
            # 대각선
            for i in range(1, N+1):
                if 1 <= now_i - i <= N and 1 <= now_j - i <= N and checkboard[now_i - i][now_j - i] == 2:
                    checkboard[now_i-i][now_j-i] = c
                if 1 <= now_i + i <= N and 1 <= now_j + i <= N and checkboard[now_i + i][now_j + i] == 2:
                    checkboard[now_i + i][now_j + i] = c
            for i in range(1, N+1):
                if 1 <= now_i - i <= N and 1 <= now_j + i <= N and checkboard[now_i - i][now_j + i] == 2:
                    checkboard[now_i-i][now_j+i] = c
                if 1 <= now_i + i <= N and 1 <= now_j - i <= N and checkboard[now_i + i][now_j - i] == 2:
                    checkboard[now_i + i][now_j - i] = c
        else:
            for j in range(1, N+1):
                # 가로
                if checkboard[now_i][j] == 1:
                    checkboard[now_i][j] = c
                # 세로
                if checkboard[j][now_j] == 1:
                    checkboard[j][now_j] = 2
            # 대각선(오른쪽 아래)
            for i in range(1, N+1):
                # print(now_i-i, now_j-i, now_i+i, now_j+i, N)
                if 1 <= now_i - i <= N and 1 <= now_j - i <= N and checkboard[now_i - i][now_j - i] == 1:
                    checkboard[now_i-i][now_j-i] = c
                if 1 <= now_i + i <= N and 1 <= now_j + i <= N and checkboard[now_i + i][now_j + i] == 1:
                    checkboard[now_i + i][now_j + i] = c
                    # print('대각선')
            for i in range(1, N+1):
                # print(now_i-i, now_j-i, now_i+i, now_j+i, N)
                if 1 <= now_i - i <= N and 1 <= now_j + i <= N and checkboard[now_i - i][now_j + i] == 1:
                    checkboard[now_i-i][now_j+i] = c
                if 1 <= now_i + i <= N and 1 <= now_j - i <= N and checkboard[now_i + i][now_j - i] == 1:
                    checkboard[now_i + i][now_j - i] = c
        pprint(checkboard)
        print()
    w, b = 0, 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if checkboard[i][j] == 2:
                w += 1
            elif checkboard[i][j] == 1:
                b += 1
    print('#{} {} {}'.format(T, b, w))
