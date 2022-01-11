'''
7
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

N = int(input())
edges = list(map(int, input().split()))

# option 1. 인접행렬
adj_mat = [[0 for _ in range(N+1)] for _ in range(N+1)]
for i in range(0, len(edges)-1, 2):
    s, e = edges[i], edges[i+1]
    adj_mat[s][e] = 1
    adj_mat[e][s] = 1

# 인접행렬 확인
for i in range(N+1):
    for j in range(N+1):
        print(adj_mat[i][j], end=" ")
    print()

# option 2. 인접리스트
adj_list = {x: [] for x in range(1, N+1)}
for i in range(0, len(edges)-1, 2):
    s, e = edges[i], edges[i+1]
    adj_list[s].append(e)
    adj_list[e].append(s)

# 인접리스트 확인
from pprint import pprint
pprint(adj_list)

# DFS (반복문)
print('============= DFS 반복문 ============')

s = 1 # 시작 번호 (현재 1 ~ 7 까지)
stack = [s]
visited = [0] * (N + 1)

while stack:
    v = stack.pop()

    if not visited[v]:

        # 방문 처리 (== 할 일 진행)
        visited[v] = 1
        print(v, end=" => ")

        # 현재 노드의 이웃 노드 탐색
        for u in range(1, N+1):
            if adj_mat[v][u] and not visited[u]:
                stack.append(u)
print()
print('=============================')

# DFS (재귀)
print('============== DFS 재귀 =============')


def dfs_recursive(v):
    # 방문 처리
    visited[v] = 1
    print(v, end=" => ")

    # 이웃 노드 탐색
    for u in range(1, N+1):
        if adj_mat[v][u] and not visited[u]:
            dfs_recursive(u)


visited = [0] * (N + 1)
dfs_recursive(1)
