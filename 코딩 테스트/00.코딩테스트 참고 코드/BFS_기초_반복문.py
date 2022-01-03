from collections import deque


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

graph = []
