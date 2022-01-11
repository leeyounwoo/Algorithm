import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    board = [[0]*N for _ in range(N)]
    board[N//2 - 1][N//2 - 1] = 2       # 1 흑돌 2 백돌
    board[N//2][N//2] = 2
    board[N//2 - 1][N//2] = 1
    board[N//2][N//2 - 1] = 1

    dyx = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]

    for _ in range(M):
        i, j, color = map(int, input().split())
        i, j = i - 1, j - 1
        if color == 1:
            pass