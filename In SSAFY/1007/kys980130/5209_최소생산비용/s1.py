import sys
sys.stdin = open('input.txt')
def dfs(num):
    global total, result

    if num == N:
        if result > total:
            result = total
        return

    if result <= total:
        return

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            total += price[num][i]
            dfs(num+1)
            visited[i] = 0
            total -= price[num][i]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    price = [list(map(int, input().split())) for _ in range(N)]
    visited = [0 for _ in range(N)]
    result = 987654321
    total = 0
    dfs(0)
    print('#{} {}'.format(tc, result))