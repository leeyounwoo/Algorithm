import sys

sys.stdin = open('input.txt')

def dfs(v):
    visited[v] = 1
    print(v, end=' ')

    for w in range(1, V+1):
        if G[v][w] == 1 and visited[w] == 0:
            dfs(w)

V, E = map(int, input().split())
tmp = list(map(int, input().split()))

G = [[0] * (V + 1) for _ in range(V+1)]
visited = [0 for _ in range(V+1)]

for i in range(0, len(tmp)-1, 2):
    G[tmp[i]][tmp[i+1]] = 1
    G[tmp[i+1]][tmp[i]] = 1

dfs(1)