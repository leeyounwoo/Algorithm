import sys
sys. stdin = open('input.txt')

def checker(puzzle):
    # 가로 체크
    for i in range(9):
        check = {}
        for j in range(9):
            check[puzzle[i][j]] = 1
        if len(check) == 9:
            continue
        else:
            return 0

    # 세로 체크
    for i in range(9):
        check = {}
        for j in range(9):
            check[puzzle[j][i]] = 1
        if len(check) == 9:
            continue
        else:
            return 0

    # 구획 체크
    for x in range(0, 9, 3):
        for y in range(0, 9, 3):
            check = {}
            for i in range(x, x+3):
                for j in range(y, y+3):
                    check[puzzle[i][j]] = 1
            if len(check) == 9:
                continue
            else:
                return 0

    return 1

t = int(input())
for tc in range(1, t+1):
    puzzle = [list(map(int, input().split())) for _ in range(9)]
    answer = checker(puzzle)

    print('#{} {}'.format(tc, answer))