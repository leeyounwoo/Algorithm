import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):

    board = [[0] * 10 for _ in range(10)]
    cnt = 0

    N = int(input())
    for i in range(1,N+1):
        r1, c1, r2, c2, color = map(int, input().split())

        for r in range(r1, r2+1) : # 행 돌면서
            for c in range(c1, c2+1):

                # 빨간색일 때 - 비어있거나, 파란색이거나
                if color == 1:
                    if board[r][c] == 0:
                        board[r][c] = 1 #비어있으면 빨간색 ㄱㄱ
                    elif board[r][c] == 2: # 파란색이 있으면 보라색으로
                        cnt += 1 # 보라색 칸 카운트

                # 파란색일 때 - 비어있거나, 빨간색이거나
                else:
                    if board[r][c] == 0:
                        board[r][c] = 2 #비어있으면 파란색 ㄱㄱ
                    elif board[r][c] == 1: # 빨간색이 있으면 보라색으로
                        cnt += 1 # 보라색 칸 카운트

    print('#{} {}'.format(tc, cnt))

