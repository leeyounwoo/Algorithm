def bfs(v):
    queue = []
    visited = [0] * (V + 1)

    queue.append(v)

    while queue:
        new_v = queue.pop(0)

        if not visited[new_v]:  # 방문한 적이 없다면
            visited[new_v] = 1  # 방문 처리
            print('-{}'.format(new_v), end='')

            for w in range(1, 1+V):
                # 현재 노드(new_v)와 연결되어 있고
                # 다음에 방문할 노드(w)에 방문한 적 없다면
                if G[new_v][w] == 1 and visited[w] == 0:
                    queue.append(w)

V, E = 7, 8
temp = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]

G  = [[0 for _ in range(V+1)] for _ in range(V+1)]

for i in range(0, len(temp), 2):
    G[temp[i]][temp[i+1]] = 1
    G[temp[i+1]][temp[i]] = 1

bfs(1)