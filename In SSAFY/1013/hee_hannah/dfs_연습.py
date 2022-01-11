'''
7
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

N = int(input())
edges = list(map(int, input().split()))

# option 1. 인접 행렬

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

# option 2. 인접 리스트
# 메모리 차원에서는 행렬보다 리스트가 효율적이다. 대신 행렬이 더 빠름
# 1 ~ 7
# {1: [2, 3],
#  2: [1, 4, 5],
#  3: [1, 7],
#  4: [2, 6],
#  5: [2, 6],
#  6: [4, 5, 7],
#  7: [6, 3]}
adj_list = { x: [] for x in range(1, N+1)}
for i in range(0, len(edges)-1, 2):
    s, e = edges[i], edges[i+1]
    adj_list[s].append(e)
    adj_list[e].append(s)

# 인접 리스트 확인
from pprint import pprint
pprint(adj_list)

# DFS 반복 (깊이 우선 정책)
print('==================DFS 반복문===============')

s = 1 # 시작 번호 (현재 1 ~ 7까지)
stack = [s]
visited = [0] * (N + 1)

# visited = set()
# add로 해도 괜찮!

while stack:
    v = stack.pop()
    if not visited[v]: # 방문한적이 없다면

        # 방문 처리 (== 할 일 진행)
        visited[v] = 1
        print(v, end=" => ")
        # 현재 노드의 이웃 노드 탐색
        for u in range(1, N+1):
            if adj_mat[v][u] and not visited[u]: # 연결되어잇고 방문한적 없다면
                stack.append(u)
print()
print('=================================')

# DFS 재귀
print('====================DFS 재귀=========')

def dfs_recursive(v):
    # 방문 처리(==할일 진행)
    visited[v] = 1
    print(v, end=" => ")
    #이웃 노드 탐색
    for u in range(1, N + 1):
        if adj_mat[v][u] and not visited[u]:
            dfs_recursive(u)

visited = [0]*(N+1)
dfs_recursive(1) # 반복문과 재귀의 결과가 다른것도 확인~ 속도는 일반적으로 반복문이 더 빠름

