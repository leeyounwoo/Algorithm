from collections import deque


def bfs(start, end):
    q = deque()
    q.append(start)
    visited[start] = True
    distance[start] = 0

    while q:
        now_node = q.popleft()
        for i in range(len(G[now_node])):
            next_node = G[now_node][i]
            if next_node == end:
                return distance[now_node] + 1
            if not visited[next_node] and distance[now_node] + 1 < distance[next_node]:
                visited[next_node] = True
                distance[next_node] = distance[now_node] + 1
                q.append(next_node)

    return 0


for T in range(1, 1 + int(input())):
    V, E = map(int, input().split())
    G = [[] for _ in range(V + 1)]
    visited = [False] * (V + 1)
    distance = [V] * (V + 1)
    for _ in range(E):
        node1, node2 = map(int, input().split())
        G[node1].append(node2)
        G[node2].append(node1)
    start, end = map(int, input().split())
    ans = bfs(start, end)
    print('#{} {}'.format(T, ans))
