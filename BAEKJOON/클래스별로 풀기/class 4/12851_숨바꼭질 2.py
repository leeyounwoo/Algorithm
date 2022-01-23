import sys


def input():
    return sys.stdin.readline().rstrip()


def rec(n, m, cnt):
    global second
    global ans
    print(n, m, cnt)
    if cnt > second:
        return
    if n == m:
        if cnt < second:
            ans = 1
        elif cnt == second:
            ans += 1
        return

    else:
        if not visited[n+1] and 0 <= n+1 <= 3*m:
            visited[n+1] = True
            rec(n+1, m, cnt+1)
        if not visited[n-1] and 0 <= n-1 <= m:
            visited[n-1] = True
            rec(n-1, m, cnt+1)
        if not visited[n*2] and 0 <= n*2 <= m*2:
            visited[n*2] = True
            rec(n*2, m, cnt+1)



sys.stdin = open('input.txt')
n, m = map(int, input().split())
second = 100_000
ans = 0
visited = [False] * 100_001
rec(n, m, 0)
print(ans)