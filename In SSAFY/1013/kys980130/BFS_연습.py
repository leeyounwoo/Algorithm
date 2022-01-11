'''
7
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

N = int(input())
edges = list(map(int, input().split()))

adj_list = { x : [] for x in range(1, N+1)}
for i in range(0, len(edges)-1, 2):
    s, e = edges[i], edges[i+1]
    adj_list[s].append(e)
    adj_list[e].append(s)

# BFS
s = 1
queue = [s]
visited = [0] * (N + 1)
visited[s] = 1

while queue:
    v = queue.pop(0)
    print(v, end=' => ')
# queue.pop(0) => O(n)

    # 인접한 이웃 노드 탐색
    for u in adj_list[v]:
        if not visited[u]:
            queue.append(u)
            visited[u] = 1
