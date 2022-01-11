import sys
sys.stdin = open('input.txt')

import copy

dij = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def bomb(i, j, power, board):
    board[i][j] = 0

    for x in range(1, power):
        for di, dj in dij:
            ni = i + di * x
            nj = j + dj * x

            if 0 <= ni < H and 0 <= nj < W:
                bomb(ni, nj, board[ni][nj], board)


def clean(board):
    w = len(board[0])
    h = len(board)
    new_board = [[0 for _ in range(w)] for _ in range(h)]
    for j in range(w):
        stack = []
        for i in range(h):
            if board[i][j]:
                stack.append(board[i][j])

        for i in range(h-1, -1, -1):
            if stack:
                new_board[i][j] = stack.pop(-1)

    return new_board


def recursion(idx, depth, board):
    global result
    if depth == N:
        cnt = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]:
                    cnt += 1
        result = min(result, cnt)
        return

    flag = 0
    for i in range(H):
        if board[i][idx]:
            bomb(i, idx, board[i][idx], board)
            flag = 1
            break

    if flag:
        for j in range(W):
            recursion(j, depth+1, clean(board))


T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    bricks = [list(map(int, input().split())) for _ in range(H)]

    result = 180
    for j in range(W):
        recursion(j, 0, copy.deepcopy(bricks))

    cnt = 0
    for i in range(len(bricks)):
        for j in range(len(bricks[0])):
            if bricks[i][j]:
                cnt += 1

    if cnt == result:
        result = 0

    print('#{} {}'.format(tc, result))