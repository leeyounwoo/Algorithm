import sys
sys.stdin = open('input.txt')


def dfs(v):
    visited[v] = 1
    print(v, end=' ')

    for w in range(1, V+1):
        if G[v][w] == 1 and visited[w] == 0:
            dfs(w)


T = 1
for tc in range(T):
    V, E = map(int, input().split())
    temp = list(map(int, input().split()))

    G = [[0 for _ in range(V+1)] for _ in range(V+1)]
    visited = [0 for _ in range(V+1)]

    for i in range(0, len(temp)-1, 2):
        G[temp[i]][temp[i+1]] = 1
        G[temp[i+1]][temp[i]] = 1

    for num in G:
        print(*num)
    dfs(1)