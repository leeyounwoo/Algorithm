import sys
sys.stdin = open('input.txt')


def backtracking(N, board, i):

    if i == N:
        return 1
    else:
        result = 0
        for j in range(N):
            if board[i][j] == 0:
                new_board = [[i for i in boardrow] for boardrow in board]
                for k in range(N-i):
                    new_board[i+k][j] = 1
                    if j+k < N:
                        new_board[i+k][j+k] = 1
                    if j-k >= 0:
                        new_board[i+k][j-k] = 1
                temp = backtracking(N, new_board, i+1)
                result += temp
        return result


T = int(input())

answer = []
for tc in range(1, T + 1):

    N = int(input())

    board = [[0 for _ in range(N)] for _ in range(N)]

    result = backtracking(N, board, 0)

    answer.append(result)

for tc in range(1, T+1):
    print(f'#{tc} {answer[tc-1]}')
