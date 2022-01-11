'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

def bfs(v): # v : 출발 노드
    queue = []
    visited = [0] * (V+1) # V: 노드의 개수
    queue.append(v)

    while queue:
        new_v = queue.pop(0)

        if not visited[new_v]: # 방문한 적이 없다면
            visited[new_v] = 1 # 방문처리(현재 노드를 방문했다)
            print(new_v, end=" ")

            for nb in range(1, 1+V): # nb: 이웃 노드
                # 현재 노드(new_v)와 연결되어있고 (G[new_v][nb] == 1)
                # 다음에 방문할 노드 nb 가 방문한 적이 없다면(visited[nb] == 0)
                if G[new_v][nb] == 1 and visited[nb] == 0:
                    queue.append(nb) #

V, E = map(int, input().split())
temp = list(map(int, input().split()))
G = [[0 for i in range(V+1)] for j in range(V+1)]
# 인접 행렬
for i in range(0, len(temp), 2):  # 입력
    G[temp[i]][temp[i+1]] = 1
    G[temp[i+1]][temp[i]] = 1 # 방향성이 없는 그래프이므로
bfs(1)