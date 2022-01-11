import sys
sys.stdin = open('input.txt')


def recursion(i, j, total):
    global result
    if total > result:
        return

    if i == N-1 and j == N-1:
        result = min(result, total)
        return

    dij = [(0, 1), (1, 0)]
    for di, dj in dij:
        ni = i + di
        nj = j + dj

        if ni < N and nj < N:
            recursion(ni, nj, total + board[ni][nj])


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    result = 1690
    recursion(0, 0, board[0][0])

    print('#{} {}'.format(tc, result))