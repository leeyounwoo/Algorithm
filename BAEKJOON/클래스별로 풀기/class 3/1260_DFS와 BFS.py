import sys
from collections import deque

sys.stdin = open('input.txt')
def dfs(start):
    d_visited[start] = True
    d_ans.append(str(start))
    for next in graph[start]:
        if not d_visited[next]:
            dfs(next)


def bfs(start, n):
    visited = [False] * (n+1)
    queue = deque([start])
    visited[start] = True
    ans = [str(start)]
    while queue:
        now = queue.popleft()
        for next in graph[now]:
            if not visited[next]:
                queue.append(next)
                visited[next] = True
                ans.append(str(next))
    return ans


n, m, v = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    i, j = map(int, sys.stdin.readline().rstrip().split())
    graph[i].append(j)
    graph[j].append(i)
for i in range(len(graph)):
    graph[i].sort()

d_visited = [False] * (n+1)
d_ans = []
dfs(v)
print(' '.join(d_ans))

ans_bfs = bfs(v, n)
print(' '.join(ans_bfs))