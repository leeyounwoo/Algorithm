import sys
sys.stdin = open('input.txt')

# handmade 최대값 반환 함수입니다.
def get_max(*args):
    temp = args[0]
    for i in range(1, len(args)):
        if temp < args[i]:
            temp = args[i]
    return temp

# 테스트 케이스는 10개입니다.
T = 10

answer = []
for tc in range(1, T + 1):

    # 들어오는 테스트 케이스 번호를 넘깁니다.
    nothing = input()
    board = []
    # 배열의 크기가 정해져 있어 고정값을 사용해 반복문을 돌립니다.
    for _ in range(100):
        board.append(list(map(int, input().split())))

    # 각 열의 합, 행의 합, 대각선의 합을 저장할 리스트를 생성합니다.
    row = [0] * 100
    col = [0] * 100
    cross = [0, 0]

    # 입력받은 2차원 배열을 탐색하면서, 각 값을 해당하는 배열의 위치에 더합니다.
    for i in range(100):
        for j in range(100):
            row[j] += board[i][j]
            col[i] += board[i][j]
            if i == j:
                cross[0] += board[i][j]
            elif i == 100 - 1 - j:
                cross[1] += board[i][j]

    # 반복문을 마치면 행의 합, 열의 합, 대각선의 합이 모두 모이므로 전체를 비교해 가장 큰 값을 찾습니다.
    result = get_max(get_max(*row), get_max(*col), get_max(*cross))

    answer.append(result)

for tc in range(1, T + 1):
    print('#{0} {1}'.format(tc, answer[tc-1]))