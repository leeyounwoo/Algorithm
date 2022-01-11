import sys
from collections import deque
sys.stdin = open('input.txt')


def bfs(start, end):
    q = deque()
    visited[start] = True
    cnt = 0
    q.append((start, cnt))

    while q:
        now_node, cnt = q.popleft()
        if now_node == end:
            return cnt

        for i in range(len(G[now_node])):
            next_node = G[now_node][i]
            if not visited[next_node]:
                visited[next_node] = True
                q.append((next_node, cnt+1))

    return 0


for T in range(1, 1+int(input())):
    V, E = map(int, input().split())
    G = [[] for _ in range(V+1)]
    visited = [False] * (V+1)
    distance = [V] * (V+1)
    for _ in range(E):
        node1, node2 = map(int, input().split())
        G[node1].append(node2)
        G[node2].append(node1)
    start, end = map(int, input().split())
    ans = bfs(start, end)
    print('#{} {}'.format(T, ans))
