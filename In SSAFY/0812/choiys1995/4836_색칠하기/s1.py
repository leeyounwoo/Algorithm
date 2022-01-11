import sys
sys.stdin = open('input.txt')

T = int(input())

# 컬러맵핑 0: 흰색 1: 빨강 2: 파랑 3: 보라
for tc in range(1, T+1):
    N = int(input())
    background = [[0]*10 for _ in range(10)]      # 흰색 2차원 배열
    result = 0

    for i in range(N):
        # 2 2 4 4 1
        r1, c1, r2, c2, color = map(int, input().split())
        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                background[r][c] += color # 비트연산: background[r][c] = background[r][c] | color
                if background[r][c] == 3:
                    result += 1

    print('#{} {}'.format(tc, result))
