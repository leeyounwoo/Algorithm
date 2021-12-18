n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
ans = 64
for start_i in range(n-7):
    for start_j in range(m-7):
        temp_board = []
        for plus_i in range(start_i, start_i+8):
            temp_board.append(board[plus_i][start_j:start_j+8])
        cnt_start_b = 0
        cnt_start_w = 0
        for i in range(8):
            for j in range(8):
                # i 홀수, j 홀수
                if i % 2 and j % 2:
                    if temp_board[i][j] == 'B':
                        cnt_start_w += 1
                    else:
                        cnt_start_b += 1
                # i 홀수, j 짝수
                elif i % 2 and j % 2 == 0:
                    if temp_board[i][j] == 'W':
                        cnt_start_w += 1
                    else:
                        cnt_start_b += 1
                # i 짝수, j 홀수
                elif i % 2 == 0 and j % 2:
                    if temp_board[i][j] == 'W':
                        cnt_start_w += 1
                    else:
                        cnt_start_b += 1
                # i 짝수, j 짝수
                elif i % 2 == 0 and j % 2 == 0:
                    if temp_board[i][j] == 'B':
                        cnt_start_w += 1
                    else:
                        cnt_start_b += 1
                # print(i, j, temp_board[i][j])
                # print('b')
        flag = min(cnt_start_b, cnt_start_w)
        if flag < ans:
            ans = flag
print(ans)