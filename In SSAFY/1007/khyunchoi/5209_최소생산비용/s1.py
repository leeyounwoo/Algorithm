import sys
sys.stdin = open('input.txt')


def calculate(depth, total):
    global result
    if result <= total:
        return

    if depth == N:
        result = min(result, total)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            calculate(depth+1, total+costs[depth][i])
            visited[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    costs = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N

    result = float('inf')
    calculate(0, 0)

    print('#{} {}'.format(tc, result))
