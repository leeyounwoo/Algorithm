from pprint import pprint

'''
7
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

N = int(input())
edges = list(map(int, input().split()))

# 1. 인접행렬
adj_mat = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(0, len(edges)-1, 2):
    s, e = edges[i], edges[i+1]
    adj_mat[s][e] = 1
    adj_mat[e][s] = 1

for i in range(N+1):
    for j in range(N+1):
        print(adj_mat[i][j], end=' ')
    print()

# pprint(adj_mat)

# 2. 인접리스트
adj_list = { x : [] for x in range(1, N+1) }

for i in range(0, len(edges)-1, 2):
    s, e = edges[i], edges[i+1]
    adj_list[s].append(e)
    adj_list[e].append(s)

pprint(adj_list)

# DFS (깊이 우선 탐색)
print('================ DFS 반복문 ================')

s = 1
stack = [s]
visited = [0] * (N+1)

while stack:
    v = stack.pop()

    if not visited[v]:
        visited[v] = 1
        print(v, end=' -> ')

        for u in range(1, N+1):
            if adj_mat[v][u] and not visited[u]:
                stack.append(u)
print()

print('================= DFS 재귀 =================')

def dfs_recursive(v):
    visited[v] = 1
    print(v, end=' -> ')

    for u in range(1, N+1):
        if adj_mat[v][u] and not visited[u]:
            dfs_recursive(u)

visited = [0] * (N+1)
dfs_recursive(1)