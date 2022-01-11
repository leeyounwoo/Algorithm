import sys
sys.stdin = open('input.txt')

delta = [(0, -1), (0, 1), (1, 0), (-1, 0)]


def is_possible(N, i, j):
    if (0 <= i < N) and (0 <= j < N):
        return True
    return False


def dfs(N, board, combi: set, i, j, num_str):
    new_num_str = num_str + board[i][j]
    if len(new_num_str) == 7:
        combi.add(new_num_str)
        return
    for di, dj in delta:
        if is_possible(N, i + di, j + dj):
            dfs(N, board, combi, i + di, j + dj, new_num_str)
    return


T = int(input())

answer = []
for tc in range(1, T + 1):

    N = 4

    board = [input().split() for _ in range(N)]

    combi = set({})

    for i in range(N):
        for j in range(N):
            dfs(N, board, combi, i, j, '')

    result = len(combi)

    answer.append(result)

for tc in range(1, T + 1):
    print(f'#{tc} {answer[tc-1]}')