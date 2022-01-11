import sys
sys.stdin = open('input.txt')

TC = int(input())

for tc in range(TC):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    # 행
    for i in range(N):
        temp_row = 0
        temp_col = 0
        for j in range(N):
            if puzzle[i][j] == 1:
                temp_row += 1
            else:
                if temp_row == K:
                    ans += 1
                temp_row = 0
            if puzzle[j][i] == 1:
                temp_col += 1
            else:
                if temp_col == K:
                    ans += 1
                temp_col = 0
        if temp_row == K:
            ans += 1
        if temp_col == K:
            ans += 1
    print('#{} {}'.format(tc+1, ans))