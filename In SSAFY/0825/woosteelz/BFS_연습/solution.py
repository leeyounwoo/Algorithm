import sys
sys.stdin = open('input.txt')

V, E = map(int, input().split())
temp = list(map(int, input().split()))
graph = [[] for _ in range(V+1)]
visited = [False for _ in range(V+1)]

for i in range(E):
    a, b = temp[i*2], temp[i*2+1]
    graph[a].append(b)
    graph[b].append(a)

queue = []
queue.append(1)
visited[1] = True

while queue:
    curr = queue.pop(0)
    print(curr, end=' ')
    for node in graph[curr]:
        if not visited[node]:
            queue.append(node)
            visited[node] = True