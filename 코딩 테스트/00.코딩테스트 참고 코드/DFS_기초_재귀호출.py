def dfs(start):
    visited[start] = True
    ans.append(str(start))
    for next in graph[start]:
        if not visited[next]:
            dfs(next)

graph = []
visited = []
ans = []
