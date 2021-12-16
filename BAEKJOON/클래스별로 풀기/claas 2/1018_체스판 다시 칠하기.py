n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
ans = 0
print(board)
for start_i in range(n-7):
    for start_j in range(m-7):
        temp = 0
        flag_start_b = True
        flag_start_w = False
        for i in range(start_i, start_i+8):
            for j in range(start_j, start_j+8):
                if board[i][j] == 'B':

        print(board[start_i:start_i+8][start_j:start_j+8])