import sys
sys.stdin = open('input.txt')


def cost(x, total):
    global result
    if total <= result:
        return

    if x == N:
        result = max(total, result)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            cost(x+1, total*(arr[x][i]/100))
            visited[i] = False


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [False] * N
    result = 0
    cost(0, 1)
    print("#{} {:.6f}".format(tc, result * 100))
