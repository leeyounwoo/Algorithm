import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


def bfs(start, end, n):
    # print('start', start, end)
    visited = [False] * (n+1)
    queue = deque([[start, 0]])
    visited[start] = True
    while queue:
        now, cnt = queue.popleft()
        if now == end:
            # print(start, end, cnt)
            ans[start][end] = cnt
            ans[end][start] = cnt
            return
        for next in graph[now]:
            if not visited[next]:
                queue.append([next, cnt+1])
                visited[next] = True


sys.stdin = open('input.txt')
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    left, right = map(int, input().split())
    graph[left].append(right)
    graph[right].append(left)
# print(graph)
ans = [[0] * (n+1) for _ in range(n+1)]
# print(ans)
answer = []
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            continue
        elif j in graph[i]:
            ans[i][j] = 1
        elif not ans[i][j]:
            flag = 0
            bfs(i, j, n)
    # print(ans)
    answer.append(sum(ans[i]))
print(answer.index(min(answer)) + 1)