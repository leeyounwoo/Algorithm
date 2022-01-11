'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

def dfs(v):
    # 방문처리
    visited[v] = 1
    print(v, end= ' ')
    # 시작정점(v) 인접한 모든 정점(w)에 대해서,
    # 방문 안 한 정점이면 재귀호출
    for w in range(1, V+1):
        # 인접하고, 방문 안 한 정점
        if adj[v][w] == 1 and visited[w] == 0:
            dfs(w)

# 정점수, 간선수, 간선들
V, E = map(int, input().split())
edges = list(map(int, input().split()))
# visited
visited = [0] * (V+1)

# 인접행렬 초기화& 7 * 7
adj = [[0] * (V+1) for _ in range(V+1)]

# 인접행렬 저장
for i in range(E):
    s, e = edges[2 * i], edges[2 * i + 1]
    adj[s][e] = 1
    adj[e][s] = 1
# 인접행렬 확인
for i in range(V+1):
    print('{0} | {1}'.format(i, adj[i]))

dfs(1)