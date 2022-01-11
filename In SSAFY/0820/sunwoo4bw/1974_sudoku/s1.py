import sys
sys.stdin = open('input.txt')

def check():
    for i in range(9):
        # 체크를 위한
        row = [0] * 10
        col = [0] * 10

        for j in range(9):
            # 행을 검사
            num_row = sudoku[i][j]
            # 열을 검사
            num_col = sudoku[j][i]

            # 이미 사용한 숫자라면 너 멈춰
            if row[num_row]: return 0
            if col[num_col]: return 0

            row[num_row] = 1
            col[num_col] = 1
            ##################
            # 3 * 3 검사도 한번에 처리 하자~~~!!!
            if i % 3 == 0 and j % 3 == 0:
                square = [0] * 10

                for r in range(i, i+3) :
                    for c in range(j, j+3):
                        num = sudoku[r][c]
                        # 중복된 숫자가 나온다면 그만~!
                        if square[num]: return 0
                        square[num] = 1
                        # 이미 사용이 되었다면, 멈춰!
                        # return값의 장점 중 하나가 만약 유효하지 않으면
                        # 그 순간 그 뒤는 안 봐도 돼!
    # 이 반복문이 끝날 때까지 return에 걸리지 않았다?!
    # -> 이 친구는 유효하다~!
    return 1


T = int(input())
for tc in range(1, T + 1):
    sudoku = [list(map(int, input().split())) for _ in range(9)] # 9* 9

    print('#{} {}'.format(tc, check()))
