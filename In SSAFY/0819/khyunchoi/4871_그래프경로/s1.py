import sys
sys.stdin = open('input.txt')

# 재귀가 안된다!
def dfs(v):
    visited[v] = 1
    flag = 0
    for w in range(1, V+1):
        if G[v][w] == 1 and visited[w] == 0:
            if w == end:
                return 1
            dfs(w)

    return flag


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    G = [[0 for _ in range(V+1)] for _ in range(V+1)]
    visited = [0 for _ in range(V+1)]

    for i in range(E):
        a, b = map(int, input().split())
        G[a][b] = 1

    start, end = map(int, input().split())

    print(dfs(start))