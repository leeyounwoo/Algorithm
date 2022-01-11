import sys
sys.stdin = open('input.txt')

def dfs(staff):
    global total, result

    if staff == N:
        if result < total:
            result = total
        return
    if result > total:
        return

    for i in range(N):
        if work[i][staff] != 0:
            if visited[i] == 0:
                visited[i] = 1
                total *= work[i][staff] * 1/100
                dfs(staff+1)
                visited[i] = 0
                total /= work[i][staff] * 1/100

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    work = [list(map(int, input().split())) for _ in range(N)]
    visited = [0 for _ in range(N)]
    total = 1
    result = 0
    dfs(0)
    print('#{} {:.6f}'.format(tc, result*100))
