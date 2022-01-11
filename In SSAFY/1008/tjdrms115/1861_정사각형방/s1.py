import sys
sys.stdin = open('input.txt')

delta = [(0, -1), (0, 1), (1, 0), (-1, 0)]


def is_possible(N, i, j):
    if (0 <= i < N) and (0 <= j < N):
        return True
    return False


def dfs(N, board, start_i, start_j):
    stack = []
    stack.append((start_i, start_j, 1))
    result = 0
    while stack:
        i, j, distance = stack.pop()
        for di, dj in delta:
            if is_possible(N, i + di, j + dj) and board[i][j] + 1 == board[i + di][j + dj]:
                stack.append((i + di, j + dj, distance + 1))
                break
        else:
            result = distance
    return result


T = int(input())

answer = []
for tc in range(1, T + 1):

    N = int(input())

    board = [list(map(int, input().split())) for _ in range(N)]

    max_dist = 0
    max_start = N * N + 1
    for i in range(N):
        for j in range(N):
            cur_dist = dfs(N, board, i, j)
            if max_dist < cur_dist:
                max_dist = cur_dist
                max_start = board[i][j]
            elif max_dist == cur_dist and max_start > board[i][j]:
                max_start = board[i][j]

    result = ' '.join(map(str, [max_start, max_dist]))

    answer.append(result)

for tc in range(1, T + 1):
    print(f'#{tc} {answer[tc-1]}')