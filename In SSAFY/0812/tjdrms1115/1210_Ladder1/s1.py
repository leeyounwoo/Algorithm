import sys
sys.stdin = open('input.txt')

# T = int(input())
T = 10

answer = []
for tc in range(1, T+1):

    # 테스트 케이스 번호입니다. 쓰지 않습니다.
    testcase = int(input())
 
    # 사다리타기 판의 크기입니다.
    N = 100
    # 판의 크기에 맞게 2차원 배열을 생성합니다.
    board = [list(map(int, input().split())) for _ in range(N)]

    # 시작 위치를 초기화합니다. 도착위치에서 출발할 것입니다.
    i, j = N-1, 0
    for a in range(N):
        if board[i][a] == 2:
            j = a
            break

    # 사다리를 타고 올라갑니다. 시작 높이에 이르면 반복을 멈춥니다.
    while i > 0:

        # 옆길이 나오면 옆길을 횡단합니다.
        if j+1 < N and board[i][j+1] == 1:
            while j+1 < N and board[i][j+1] == 1:
                j += 1
        elif j - 1 >= 0 and board[i][j - 1] == 1:
            while j - 1 >= 0 and board[i][j - 1] == 1:
                j -= 1
        # 사다리를 한 칸 오릅니다.
        i -= 1

    # 시작위치를 출력합니다.
    result = j
    answer.append(result)

for tc in range(1, T+1):
    print('#{0} {1}'.format(tc, answer[tc-1]))
