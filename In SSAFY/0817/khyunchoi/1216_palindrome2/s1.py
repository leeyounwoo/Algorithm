import sys
sys.stdin = open('input.txt')


def is_pal(text):
    if text == text[::-1]:
        return len(text)
    return 0


for tc in range(1, 11):
    size = 100
    T = int(input())
    board = [input() for i in range(size)]

    result = 0
    for i in range(size):
        for j in range(size):
            word_row = ''           # 가로 판단
            tmp_result_row = 0
            for k in range(j, size):
                word_row += board[i][k]
                if len(word_row) > result:
                    tmp_result_row = max(tmp_result_row, is_pal(word_row))

            word_col = ''           # 세로 판단
            tmp_result_col = 0
            for k in range(i, size):
                word_col += board[k][j]
                if len(word_col) > result:
                    tmp_result_col = max(tmp_result_col, is_pal(word_col))

            result = max(result, tmp_result_row, tmp_result_col)

    print('#{} {}'.format(tc, result))