import sys
sys.stdin = open('input.txt')


def recursion(v, depth, total):
    global result

    if depth == N-1:
        result = min(result, total + board[v][0])
        return

    for i in range(1, N):
        if not visited[i]:
            visited[i] = 1
            recursion(i, depth+1, total+board[v][i])
            visited[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N

    result = 10000
    recursion(0, 0, 0)

    print('#{} {}'.format(tc, result))
