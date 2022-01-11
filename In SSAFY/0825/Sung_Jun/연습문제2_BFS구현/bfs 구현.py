'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''


def bfs(v):
    queue = []
    visited = [0] * (V+1)
    queue.append(v)

    while queue:
        new_v = queue.pop()

        if not visited[new_v]:
            visited[new_v] = 1
            print(new_v, end=" ")

            for nb in range(1, 1+V):
                if G[new_v][nb] == 1 and visited[nb] == 0:
                    queue.append(nb)

V, E = map(int, input().split())
temp = list(map(int, input().split()))
G = [[0 for i in range(V+1)] for j in range(V+1)]
bfs(temp)

