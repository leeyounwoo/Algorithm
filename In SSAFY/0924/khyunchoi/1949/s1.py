import sys
sys.stdin = open('input.txt')


def dfs(i, j, height, cut, length):
    global max_length
    max_length = max(length, max_length)

    visited[i][j] = True
    dij = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for di, dj in dij:
        ni = i + di
        nj = j + dj
        if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
            if board[ni][nj] < height:
                visited[ni][nj] = True
                dfs(ni, nj, board[ni][nj], cut, length+1)
                visited[ni][nj] = False
            else:
                if cut and (board[ni][nj] - K) < height:
                    visited[ni][nj] = True
                    dfs(ni, nj, height-1, False, length+1)
                    visited[ni][nj] = False


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False for _ in range(N)] for _ in range(N)]

    max_height = 0
    for i in range(N):
        for j in range(N):
            max_height = max(max_height, board[i][j])

    max_length = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == max_height:
                dfs(i, j, max_height, True, 1)
                visited[i][j] = False

    print('#{} {}'.format(tc, max_length))
