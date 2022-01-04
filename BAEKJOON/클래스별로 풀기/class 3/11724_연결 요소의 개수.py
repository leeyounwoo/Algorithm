import sys


def dfs(start):
    visited[start] = True
    for next in graph[start]:
        if not visited[next]:
            dfs(next)


sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.stdin = open('input.txt')
n, m = map(int, input().rstrip().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b= map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False] * (n+1)
ans = 0
for i in range(1, n+1):
    if not visited[i]:
        ans += 1
        dfs(i)
print(ans)