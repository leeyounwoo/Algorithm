import sys
sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t+1):
    n, k = map(int, input().split())

    puzzle = [list(map(int, input().split())) for _ in range(n)]
    ans = 0

    for i in range(n):
        # 행을 검사
        cnt_r = 0
        for j in range(n):
            if puzzle[i][j] == 1: # 흰색부분이야
                cnt_r += 1
            else:
                if cnt_r == k:
                    ans += 1
                cnt_r = 0

        #끝까지 가서야 완성이 된 경우
        if cnt_r == k:
            ans += 1

        # 열을 검사
        cnt_c = 0
        for j in range(n):
            if puzzle[j][i] == 1:
                cnt_c += 1
            else:
                if cnt_c == k:
                    ans += 1
                cnt = 0
        if cnt_c == k:
            ans += 1

    print('#{} {}'.format(tc, ans))
