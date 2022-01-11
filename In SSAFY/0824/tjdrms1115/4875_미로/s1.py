import sys
sys.stdin = open('input.txt')


# 시작점을 찾는 함수입니다.
# return으로 간편하게 처리하려고 만들었습니다.
def find_start(N, board):
    for i in range(N):
        for j in range(N):
            if board[i][j] == 2:
                return i, j


# 백트래킹 중 방문한 위치가 적합한 곳인지 확인하는 함수입니다.
def promising(N, board, i, j):
    # 적합한 곳이면 True를 반환합니다.
    if (0 <= i < N) and (0 <= j < N) and board[i][j] != 1:
        return True
    # 부적합하다면 False를 반환합니다.
    return False


# 백트래킹 기법으로 길을 찾습니다.
def backtracking(N, board, i, j):
    # 방문한 노드가 유망한지 검사합니다.
    if promising(N, board, i, j):
        # 유망하다면 다음을 수행합니다.

        # 도착지에 도착했으면 1을 반환합니다.
        if board[i][j] == 3:
            return 1
        # 아직 도착 안했다면 4방향으로 한 번씩 이동합니다.
        else:
            board[i][j] = 1
            delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            for di, dj in delta:
                check = backtracking(N, board, i+di, j+dj)
                # 1을 반환받았으면 더 이상 진행 않고 1을 반환합니다.
                if check:
                    return 1
    # 1을 반환못했다면 0을 반환합니다.
    return 0


# 테스트 케이스를 입력받습니다.
T = int(input())

# 답을 저장할 리스트입니다.
answer = []
# 테스트 케이스 수 만큼 코드를 실행합니다.
for tc in range(1, T+1):

    # 미로의 크기와 미로를 입력받습니다.
    N = int(input())
    board = [list(map(int, input())) for _ in range(N)]

    # 시작점을 결정합니다.
    s_i, s_j = find_start(N, board)

    # 백트래킹으로 경로를 탐색합니다.
    result = backtracking(N, board, s_i, s_j)

    # 결과를 출력합니다.
    answer.append(result)

for tc in range(1, T + 1):
    print('#{} {}'.format(tc, answer[tc-1]))
