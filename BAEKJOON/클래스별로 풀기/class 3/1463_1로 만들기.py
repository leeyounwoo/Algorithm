import sys

def bfs(n, cnt):
    global ans
    if cnt >= ans:
        return
    if n == 1:
        if cnt < ans:
            ans = cnt
        return
    else:
        if n % 3 == 0:
            bfs(n//3, cnt+1)
        if n % 2 == 0:
            bfs(n//2, cnt+1)
        bfs(n-1, cnt+1)

sys.stdin = open('input.txt')
n = int(input())
ans = n
bfs(n, 0)
print(ans)