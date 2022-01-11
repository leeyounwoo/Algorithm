import sys
sys.stdin = open('input.txt')


def dfs(v):
    stack = []
    stack.append(v)

    while stack:
        v = stack.pop()

        if visited[v] == 0:
            visited[v] = 1

            for w in range(V):
                if G[v][w] == 1 and visited[w] == 0:
                    if w == 99:
                        return 1
                    stack.append(w)
    return 0


T = 10
for tc in range(1, T+1):
    V = 100
    _, E = map(int, input().split())
    temp = list(map(int, input().split()))
    G = [[0]*100 for _ in range(100)]
    visited = [0 for _ in range(100)]

    for i in range(0, len(temp), 2):
        G[temp[i]][temp[i+1]] = 1

    print('#{} {}'.format(tc, dfs(0)))