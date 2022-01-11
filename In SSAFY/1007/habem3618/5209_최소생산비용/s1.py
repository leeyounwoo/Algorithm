import sys
sys.stdin = open('input.txt')


def cost(x, total):
    global result
    if total >= result:
        return

    if x == N:
        result = min(total, result)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            cost(x+1, total+arr[x][i])
            visited[i] = False


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [False] * N
    result = 1500
    cost(0, 0)
    print("#{} {}".format(tc, result))
