T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [list(input()) for _ in range(N)]
    dyx = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for i in range(N):
        for j in range(N):
            if board[i][j] == 'A':
                for dy, dx in dyx:
                    ny = i + dy
                    nx = j + dx
                    if 0 <= ny < N and 0 <= nx < N:
                        pass

    print(board)