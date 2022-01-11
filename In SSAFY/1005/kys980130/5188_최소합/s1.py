import sys
sys.stdin = open('input.txt')
dyx = ((0, 1), (1, 0))

def dfs(x, y, total):
    global min_sum
    if min_sum < total:
        return

    if x == y == N-1:
        if min_sum > total:
            min_sum = total
            return


    for dy, dx in dyx:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < N and 0 <= ny < N:
            dfs(nx, ny, total + board[nx][ny])


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    min_sum = 10000
    dfs(0, 0, board[0][0])
    print('#{} {}'.format(tc, min_sum))