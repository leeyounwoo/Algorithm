import sys
sys.stdin = open('input.txt')


def dfs(v):
    stack = []
    stack.append(v)

    while stack:
        v = stack.pop()

        if visited[v] == 0:
            visited[v] = 1

            for w in range(1, V+1):
                if G[v][w] == 1 and visited[w] == 0:
                    if w == end:
                        return 1
                    stack.append(w)
    return 0


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    G = [[0 for _ in range(V+1)] for _ in range(V+1)]
    visited = [0 for _ in range(V+1)]

    for i in range(E):
        a, b = map(int, input().split())
        G[a][b] = 1

    start, end = map(int, input().split())

    print('#{} {}'.format(tc, dfs(start)))