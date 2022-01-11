import sys
sys.stdin = open('input.txt')


# 백트래킹을 통해 배열의 최소합을 찾습니다.
def backtracking(N, board, visited, i, total):
    # 전역 변수 result를 선언합니다.
    # 최소합을 저장할 변수입니다.
    global result
    # 현재 상태가 유망한지 검사합니다.
    # 백트래킹 중 얻은 숫자의 합 total이 저장된 최소합을 넘겼으면
    # 즉시 종료합니다.
    if total < result:
        # 아직 현재까지의 합이 저장된 최소합보다 작다면 이어서 탐색합니다.

        # i가 N이면 모든 탐색을 마쳤으므로
        # result에 지금까지의 합 total을 저장합니다.
        if i == N:
            result = total
        # 아니라면 다음 행에서 아직 탐색하지 않은 열을 찾아
        # 백트래킹을 이어갑니다.
        else:
            for j in range(N):
                if not visited[j]:
                    # 다음 백트래킹으로 넘어갈 떄
                    # total에 선택한 위치의 값을 추가합니다.
                    visited[j] = 1
                    backtracking(N, board, visited, i+1, total + board[i][j])
                    visited[j] = 0


# 테스트 케이스를 입력받습니다.
T = int(input())

# 답을 저장할 리스트입니다.
answer = []
# 테스트 케이스 수 만큼 코드를 실행합니다.
for tc in range(1, T+1):

    # 배열의 크기와 2차원 배열을 입력받습니다.
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    # 방문 여부를 저장할 리스트와 최소값을 초기화합니다.
    visited = [0] * N
    result = 1000

    # 백트래킹을 통해 result에 최소값을 저장합니다.
    backtracking(N, board, visited, 0, 0)

    # 결과를 출력합니다.
    answer.append(result)

for tc in range(1, T + 1):
    print('#{} {}'.format(tc, answer[tc-1]))
