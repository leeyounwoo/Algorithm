import sys
sys.stdin = open('input.txt')


def judgement(num_set):
    if len(num_set) == 9:
        return 1
    return 0


T = int(input())
for tc in range(1, T+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    result = 1

    for i in range(9):
        sudoku_row = set()
        sudoku_col = set()
        for j in range(9):
            sudoku_row.add(sudoku[i][j])
            sudoku_col.add(sudoku[j][i])

        if not judgement(sudoku_row) or not judgement(sudoku_col):
            result = 0
            break

    for i in range(3):
        for j in range(3):
            sudoku_box = set()
            for x in range(i*3, i*3+3):
                for y in range(j*3, j*3+3):
                    sudoku_box.add(sudoku[x][y])

            if not judgement(sudoku_box):
                result = 0
                break

    print('#{} {}'.format(tc, result))