import sys
sys.stdin = open('input.txt')


def border_check(N, i, j):
    if (0 <= i < N) and (0 <= j < N):
        return True
    return False


def find_path(N, board, start_i, start_j):
    delta = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    queue = []
    # i, j, path distance
    queue.append([start_i, start_j, 1])
    max_length = 0
    while queue:
        i, j, length = queue.pop(0)
        if max_length < length:
            max_length = length
        for di, dj in delta:
            if border_check(N, i + di, j + dj) and board[i + di][j + dj] < board[i][j]:
                queue.append([i + di, j + dj, length + 1])
    return max_length


T = int(input())

answer = []
for tc in range(1, T + 1):

    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    start_list = []
    tempmax = 0
    for i in range(N):
        for j in range(N):
            if tempmax < board[i][j]:
                tempmax = board[i][j]
                start_list.clear()
                start_list.append([i, j])
            elif tempmax == board[i][j]:
                start_list.append([i, j])

    tempmax = 0
    for i in range(N):
        for j in range(N):
            for k in range(K + 1):
                board[i][j] -= k
                for start_i, start_j in start_list:
                    if start_i != i or start_j != j:
                        temp_length = find_path(N, board, start_i, start_j)
                        if tempmax < temp_length:
                            tempmax = temp_length
                board[i][j] += k

    result = tempmax
    answer.append(result)

for tc in range(1, T + 1):
    print(f'#{tc} {answer[tc-1]}')