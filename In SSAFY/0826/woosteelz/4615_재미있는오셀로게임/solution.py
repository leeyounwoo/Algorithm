import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    N, M = map(int, input().split())
    info = {
        1 : 'B',
        2 : 'A'
    }

    # 초기보드 세팅
    board = [['-' for _ in range(N)] for _ in range(N)]
    start, end = N // 2 - 1, N // 2 - 1
    board[start][end] = 'W'
    board[start+1][end+1] = 'W'
    board[start+1][end] = 'B'
    board[start][end+1] = 'B'

    for _ in range(M):
        y, x, doll = map(int, input().split())

