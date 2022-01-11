import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):

    # 스도쿠 크기입니다. 고정값입니다.
    N = 9
    # 스도쿠 배열을 입력받습니다.
    sdoku_board = [list(map(int, input().split())) for _ in range(N)]

    # 검사 결과를 저장할 변수입니다.
    check = 1
    # 행에 대해 검사합니다.
    for i in range(N):
        # 검사할 숫자의 리스트를 만듭니다.
        checklist = [0] * N

        for j in range(N):
            # 이미 검사한 숫자가 다시 나오면 반복을 종료합니다.
            if checklist[sdoku_board[i][j] - 1]:
                check = 0
                break
            else:
                # 처음 보는 숫자라면 체크합니다.
                checklist[sdoku_board[i][j] - 1] = 1

    # 행 검사를 통과했다면 이어서 검사합니다.
    if check:
        # 열에 대해 검사합니다.
        for i in range(N):
            # 검사할 숫자의 리스트를 만듭니다.
            checklist = [0] * (N + 1)

            for j in range(N):
                # 이미 검사한 숫자가 다시 나오면 반복을 종료합니다.
                if checklist[sdoku_board[j][i] - 1]:
                    check = 0
                    break
                else:
                    # 처음 보는 숫자라면 체크합니다.
                    checklist[sdoku_board[j][i] - 1] = 1

    # 열 검사를 통과했다면 이어서 검사합니다.
    if check:
        # 사각형 검사입니다.
        for i in range(0, N, 3):
            for j in range(0, N, 3):
                # 검사할 숫자의 리스트를 만듭니다.
                checklist = [0] * N

                for k in range(3):
                    for l in range(3):
                        # 이미 검사한 숫자가 다시 나오면 반복을 종료합니다.
                        if checklist[sdoku_board[i + k][j + l] - 1]:
                            check = 0
                            break
                        else:
                            # 처음 보는 숫자라면 체크합니다.
                            checklist[sdoku_board[i + k][j + l] - 1] = 1

    # 검사 결과를 출력합니다.
    result = check
    print('#{} {}'.format(tc, result))
