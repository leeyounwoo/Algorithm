import sys
sys.stdin = open('input.txt')

def dfs_reflect(v, e):
    global result
    if v == e:
        result = 1
        return

    visited[v] = 1

    for w in range(1, V+1):
        if G[v][w] == 1 and visited[w] == 0:
            dfs_reflect(w, e)

T = int(input())

for t in range(1, T+1):
    V, E = map(int, input().split())

    G = [[0 for _ in range(V+1)] for _ in range(V+1)]
    visited = [0] * (V+1)

    for _ in range(E):
        x, y = map(int, input().split())
        G[x][y] = 1

    # for i in range(V+1):
    #     print('{} | {}'.format(i, G[i]))

    S, E = map(int, input().split())

    result = 0
    dfs_reflect(S, E)

    print('#{} {}'.format(t, result))