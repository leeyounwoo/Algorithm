import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    area = [[0]*10 for _ in range(10)]

    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())

        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                area[i][j] += color

    cnt = 0
    for i in range(10):
        for j in range(10):
            if area[i][j] == 3:
                cnt += 1

    print('#{} {}'.format(tc, cnt))