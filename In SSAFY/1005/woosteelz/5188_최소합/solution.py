import sys
sys.stdin = open('1005/woosteelz/5188_최소합/sample_input.txt')


def DFS(row, col):
    down = right = N * 11  # 범위 밖 가상의 값

    if row == col >= N-1:  # 마지막 지점 도착
        return board[row][col]
    else:
        if row < N-1:  # 아래쪽 끝이 아니면
            down = DFS(row + 1, col)
        if col < N-1:  # 오른쪽 끝이 아니면
            right = DFS(row, col + 1)

    if down < right:  # 작은 값 취함
        return down + board[row][col]
    else:
        return right + board[row][col]


def dfs(x, y, res):
    global N, ans

    res += board[x][y]
    if ans < res:
        return

    if x == N-1 and y == N-1:
        ans = min(ans, res)
    for i in range(2):
        a, b = x + dir_x[i], y + dir_y[i]
        if 0 <= a < N and 0 <= b < N and not visited[a][b]:
            visited[a][b] = True
            dfs(a, b, res)
            visited[a][b] = False
    res -= board[x][y]
    return


for tc in range(int(input())):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False for _ in range(N)] for _ in range(N)]
    dir_x = [0, 1]
    dir_y = [1, 0]
    ans = float('inf')
    dfs(0, 0, 0)

    print(f"#{tc + 1} {ans}")
