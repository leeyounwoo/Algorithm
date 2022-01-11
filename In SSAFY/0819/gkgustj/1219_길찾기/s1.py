import sys
sys.stdin = open('input.txt')

def dfs(v):
    global result

    if v==99:
        result = 1
        return

    visited[v] = 1

    for w in range(100):
        if G[v][w]==1 and visited[w]==0:
            dfs(w)


for _ in range(10):
    t, E = map(int, input().split())
    temp = list(map(int, input().split()))

    G = [[0 for _ in range(100)] for _ in range(100)]
    visited = [0] * 100

    for i in range(0, len(temp)-1, 2):
        G[temp[i]][temp[i+1]] = 1

    result = 0
    dfs(0)

    print('#{} {}'.format(t, result))