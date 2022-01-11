import sys
sys.stdin = open('input.txt')

T = int(input())

answer = []
for tc in range(1, T + 1):

    # 판의 크기와 넣는 단어의 길이를 입력받습니다.
    N, K = list(map(int, input().split()))
    # 입력받은 N을 사용해 판을 만듧니다.
    board = [list(map(int, input().split())) for _ in range(N)]

    total = 0
    # 순회하며 가로 세로에 알맞는 자리가 있는지 확인합니다.
    for i in range(N):
        for j in range(N):
            # 가로 확인입니다.
            # 직전 위치가 바깥이거나 검은 칸이면 탐색을 시작합니다.
            if (j + K - 1 < N) and (j-1 < 0 or board[i][j-1] == 0):
                for a in range(K):
                    # 흰 칸이 이어지지 않으면 멈춥니다.
                    if board[i][j + a] == 0:
                        break
                # 반복문이 멈추지 않았다면, 딱 맞는 공간인지 확인합니다.
                else:
                    if j + K >= N or board[i][j + K] == 0:
                        # 조건을 충족하므로 개수를 셉니다.
                        total += 1
            # 세로 확인입니다.
            # 직전 위치가 바깥이거나 검은 칸이면 탐색을 시작합니다.
            if (i + K - 1 < N) and (i-1 < 0 or board[i-1][j] == 0):
                for a in range(K):
                    # 흰 칸이 이어지지 않으면 멈춥니다.
                    if board[i + a][j] == 0:
                        break
                # 반복문이 멈추지 않았다면, 딱 맞는 공간인지 확인합니다.
                else:
                    if i + K >= N or board[i + K][j] == 0:
                        # 조건을 충족하므로 개수를 셉니다.
                        total += 1

    # 총 개수를 출력합니다.
    answer.append(total)

for tc in range(1, T+1):
    print('#{0} {1}'.format(tc, answer[tc-1]))
