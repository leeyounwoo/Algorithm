import sys
sys.stdin = open('input.txt')

def dfs(staff, re):
    global result

    if staff == N:
        if result < re:
            result = re
        return
    if result >= re:
        return

    for i in range(N):

        if visited[i] == 0:
            visited[i] = 1
            dfs(staff + 1, re * (board[staff][i] / 100))
            visited[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N

    result = 0
    dfs(0, 1)
    print('#{} {:.6f}'.format(tc, result*100))
