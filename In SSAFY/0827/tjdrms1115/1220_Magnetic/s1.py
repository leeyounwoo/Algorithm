import sys
sys.stdin = open('input.txt')

# T = int(input())
T = 10

answer = []
for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    check = 2
    for j in range(N):
        check = 2
        for i in range(N):
            if board[i][j] == 1 and check == 2:
                check = 1
            elif board[i][j] == 2 and check == 1:
                check = 2
                result += 1

    answer.append(result)

for tc in range(1, T+1):
    print('#{} {}'.format(tc, answer[tc-1]))
