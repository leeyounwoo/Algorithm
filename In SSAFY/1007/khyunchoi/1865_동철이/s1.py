import sys
sys.stdin = open('input.txt')


def calculate(depth, total):
    global result
    if result >= total:
        return

    if depth == N:
        result = max(result, total)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            calculate(depth+1, total * (probabilities[depth][i] / 100))
            visited[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    probabilities = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N

    result = 0
    calculate(0, 1)

    print('#{} {:.6f}'.format(tc, round(result*100, 6)))
