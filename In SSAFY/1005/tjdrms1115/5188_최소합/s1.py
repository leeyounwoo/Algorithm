import sys
sys.stdin = open('input.txt')


def get_min_path(N, board, i, j):
    if i == j == (N - 1):
        return board[i][j]
    else:
        min_path = 10000000
        if i < N - 1:
            temp = get_min_path(N, board, i + 1, j)
            if min_path > temp:
                min_path = temp
        if j < N - 1:
            temp = get_min_path(N, board, i, j + 1)
            if min_path > temp:
                min_path = temp
        return board[i][j] + min_path


T = int(input())

answer = []
for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    result = get_min_path(N, board, 0, 0)

    answer.append(result)

for tc in range(1, T + 1):
    print(f'#{tc} {answer[tc-1]}')
