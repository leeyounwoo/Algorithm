'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

def bfs(s, V):
    queue = []
    visited = [0] * (V + 1)
    queue.append(s)
    while queue:
        s = queue.pop(0)
        if not visited[s]:
            visited[s] = 1
            print(s, end=' ')
            for i in range(1, V+1):
                if adj[s][i] == 1 and visited[i] == 0:
                    queue.append(i)

V, E = map(int, input().split())
tmp = list(map(int, input().split()))
adj = [[0] * (V + 1) for _ in range(V+1)]

for i in range(E):
    n1, n2 = tmp[2*i], tmp[2*i+1]
    adj[n1][n2] = 1
    adj[n2][n1] = 1

bfs(1, V)