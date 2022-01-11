import sys
sys.stdin = open('input.txt')


def find(i, j, number):
    if len(number) == 7:
        if number not in result:
            result.append(number)
        return

    dij = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for di, dj in dij:
        ni = i + di
        nj = j + dj

        if 0 <= ni < N and 0 <= nj < N:
            find(ni, nj, number + board[ni][nj])


T = int(input())
for tc in range(1, T+1):
    N = 4
    board = [list(input().split()) for _ in range(N)]
    result = []

    for i in range(N):
        for j in range(N):
            find(i, j, board[i][j])

    print('#{} {}'.format(tc, len(result)))