import sys
sys.stdin = open('input.txt')

def is_vaild(arr):
    for i in range(9):
        temp_col = [0 for _ in range(10)]
        temp_row = [0 for _ in range(10)]
        for j in range(9):
            temp_col[arr[i][j]] = 1
            temp_row[arr[j][i]] = 1
        if not sum(temp_row) == 9:
            return 0
        if not sum(temp_col) == 9:
            return 0

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            temp = [0 for _ in range(10)]
            for n in range(3):
                for m in range(3):
                    temp[arr[n+i][m+j]] = 1
            if not sum(temp) == 9:
                return 0
    return 1

TC = int(input())
for tc in range(TC):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    print('#{} {}'.format(tc+1, is_vaild(sudoku)))
