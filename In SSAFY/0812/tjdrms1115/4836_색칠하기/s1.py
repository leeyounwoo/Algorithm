import sys
sys.stdin = open('input.txt')

T = int(input())

answer = []
for tc in range(1, T+1):

    # 색칠할 횟수를 입력받습니다.
    N = int(input())

    # 전체 판의 크기에 맞는 2차원 배열을 생성합니다.
    size = 10
    board = [[0 for _ in range(size)] for _ in range(size)]

    # N번의 색칠을 수행합니다.
    for _ in range(N):
        # 색칠에 필요한 변수를 입력받습니다.
        i1, j1, i2, j2, c = map(int, input().split())

        # 색칠합니다. 1은 빨강이고 2는 파랑입니다.
        for i in range(i1, i2+1):
            for j in range(j1, j2+1):
                # 비트 연산을 통해 1 및 2를 색칠합니다.
                board[i][j] = board[i][j] | c

    # 색칠된 결과를 통해 보라색 영역을 셉니다.
    result = 0
    for i in range(size):
        for j in range(size):
            # 1과 2가 칠해졌다면 결과는 3(보라)이 될 것입니다.
            if board[i][j] == 3:
                result += 1

    # 결과를 출력합니다.
    answer.append(result)

for tc in range(1, T+1):
    print('#{0} {1}'.format(tc, answer[tc-1]))
