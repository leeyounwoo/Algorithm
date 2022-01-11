import sys
sys.stdin = open('input.txt')


# 말이 놓여진 위치를 기반으로 판 위의 말들의 색을 바꾸는 함수입니다.
def change_color(board, color, i, j):
    # 편의를 위해 보드의 크기를 저장합니다.
    N = len(board)
    # 대각선을 포함한 방향의 리스트를 생성합니다.
    dirlist = [(a, b) for a in [-1, 0, 1] for b in [-1, 0, 1] if not (a == b == 0)]

    # 각 방향별로 색을 바꿀 말들이 있는지 검사합니다.
    for a, b in dirlist:
        check = 0
        # 상대 말을 내 말이 양끝에서 둘러쌌는지 확인합니다.
        step = 1
        while (0 <= i + (step * a) < N) and (0 <= j + (step * b) < N):
            if board[i + (step * a)][j + (step * b)] == color:
                check = 1
                break
            step += 1
        # 둘러쌌다면 경로 안의 말들을 내 말로 변경합니다.
        # 중간이 빈 칸이 있으면 변경하지 않습니다.
        if check:
            for step2 in range(step-1, 0, -1):
                if board[i + (step2 * a)][j + (step2 * b)] == 0:
                    break
            else:
                for x in range(1, step):
                    board[i + (x * a)][j + (x * b)] = color


# 테스트 케이스의 개수를 입력받습니다.
T = int(input())

# 테스트 케이스만큼 코드를 실행하고 결과를 저장합니다.
answer = []
for tc in range(1, T + 1):

    # 입력값들을 입력받습니다.
    N, M = map(int, input().split())
    queue = []
    # black : 1, white : 2
    for i in range(M):
        queue.append(list(map(int, input().split())))

    # 판을 입력받아 초기 말들을 놓습니다.
    board = [[0 for _ in range(N)] for _ in range(N)]
    board[(N // 2) - 1][(N // 2) - 1] = 2
    board[(N // 2)][(N // 2) - 1] = 1
    board[(N // 2) - 1][(N // 2)] = 1
    board[(N // 2)][(N // 2)] = 2

    # 입력값을 통해 말을 하나씩 놓으면서 오셀로 게임을 진행합니다.
    for j, i, color in queue:
        i = i - 1
        j = j - 1
        board[i][j] = color
        change_color(board, color, i, j)

    # 게임이 끝나고 말 수를 셉니다.
    b = 0
    w = 0
    for line in board:
        for pos in line:
            if pos == 1:
                b += 1
            elif pos == 2:
                w += 1
    result = '{} {}'.format(b, w)
    # 결과를 출력합니다.
    answer.append(result)

for tc in range(1, T + 1):
    print('#{} {}'.format(tc, answer[tc-1]))
