import sys
sys.stdin = open('input.txt')

def dfs(v):
    visited[v] = True
    print(v, end=' ')

    for w in range(1, V+1):
        if not visited[w] and graph[v][w]:
            dfs(w)

V, E = map(int, input().split())
temp = list(map(int, input().split()))

graph = [[0 for _ in range(V+1)] for _ in range(V+1)]
visited = [False for _ in range(V+1)]

for i in range(E):
    graph[temp[i*2]][temp[i*2+1]] = 1
    graph[temp[i*2+1]][temp[i*2]] = 1

dfs(1)