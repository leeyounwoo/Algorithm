import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    board = [input() for _ in range(N)]

    result = ''
    flag = 0
    for i in range(N):
        for j in range(N-M+1):
            word_row = ''
            word_col = ''
            for k in range(j, j+M):
                word_row += board[i][k]
                word_col += board[k][i]

            if word_row == word_row[::-1]:
                result = word_row
                flag = 1
                break

            if word_col == word_col[::-1]:
                result = word_col
                flag = 1
                break

        if flag:
            break

    print('#{} {}'.format(tc, result))