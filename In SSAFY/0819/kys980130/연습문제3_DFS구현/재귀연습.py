import sys
sys.stdin = open("input.txt")

def dfs(v):
    visited[v] = 1
    for w in range(1, V+1):
        if G[v][w] == 1 and visited[v] == 0:
            dfs(w)