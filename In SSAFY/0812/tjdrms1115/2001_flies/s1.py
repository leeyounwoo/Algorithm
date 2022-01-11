import sys
sys.stdin = open('input.txt')

T = int(input())

answer = []
for tc in range(1, T+1):

    # 판의 크기 N과 파리채의 크기 M을 입력받습니다.
    N, M = map(int, input().split())

    # 판의 크기에 맞게 2차원 배열을 입력받습니다.
    board = [list(map(int, input().split())) for _ in range(N)]

    # 각 위치 별 잡을 수 있는 파리 수를 계산해서 최대값을 구합니다.
    result = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            # board[i][j]를 기준의로 M의 범위만큼의 파리를 모두 더합니다.
            for a in range(M):
                for b in range(M):
                    if not (a == b == 0):
                        board[i][j] += board[i+a][j+b]
            # 범위 안의 파리 총합이 현재 최대값보다 크면 갱신합니다.
            if result < board[i][j]:
                result = board[i][j]
    # 결과를 출력합니다.
    answer.append(result)

for tc in range(1, T+1):
    print('#{0} {1}'.format(tc, answer[tc-1]))