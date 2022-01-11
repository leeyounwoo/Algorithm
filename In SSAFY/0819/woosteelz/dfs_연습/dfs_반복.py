import sys
sys.stdin = open('input.txt')

def dfs(v):
    stack = []
    stack.append(v)
    while stack:
        v = stack.pop()
        visited[v] = True
        for w in range(1, V+1):
            if graph[v][w] == 1 and not visited[w]:
                stack.append(w)

V, E = map(int, input().split())
temp = list(map(int, input().split()))

graph = [[0 for _ in range(V+1)] for _ in range(V+1)]
visited = [False for _ in range(V+1)]

for i in range(E):
    graph[temp[i*2]][temp[i*2+1]] = 1
    graph[temp[i*2+1]][temp[i*2]] = 1

dfs(1)