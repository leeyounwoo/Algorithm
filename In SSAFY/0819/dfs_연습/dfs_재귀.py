import sys
sys.stdin = open('input.txt')

<<<<<<< HEAD
def dfs(v):
    visited[v] = 1
    print(v, end = " ")

    # 현재 노드와 인접한 노드 찾기
    for w in range(1, V+1):
        # 만약 방문한 적 없고, 연결되어 있다면 ...
=======

def dfs(v):
    visited[v] = 1
    print(v, end=" ")  # 현재 방문 노드 출력
    
    # 현재 노드(v)와 인접한 노드 찾기
    for w in range(1, V+1):
        # 만약 방문한 적 없고, 연결되어 있다면...
        if G[v][w] == 1 and visited[w] == 0:
            # 인접한 노드(w)를 가지고서 다음 dfs 실행
            # 즉, 이웃 노드(w)가 새로운 v가 됨
            dfs(w)

<<<<<<< HEAD
V, E = map(int, input().split()) # 7, 8
temp = list(map(int, input().split())) # 1 2 1 3 ...

G = [[0 for _ in range(V+1)] for _ in range(V+1)]
visited = [0 for _ in range(V+1)]

for i in range(0, len(temp)-1, 2):
    G[temp[i]][temp[i+1]] = 1
    G[temp[i+1]][temp[i]] = 1

dfs(1)
=======

V, E = map(int, input().split())  # 7, 8
temp = list(map(int, input().split()))  # 1 2 1 3 ...

G = [[0 for _ in range(V+1)] for _ in range(V+1)] # 인접 행렬
visited = [0 for _ in range(V+1)] # [0, 0, 0, 0, 0, ...]

for i in range(0, len(temp)-1, 2):
    G[temp[i]][temp[i+1]] = 1  # 인접한 노드 표기
    G[temp[i+1]][temp[i]] = 1  # 반대 방향도 표기 (무방향 그래프이므로)

# 인접 행렬 출력 테스트
for i in range(V+1):
    for j in range(V+1):
        print(G[i][j], end=" ")
    print()

<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
dfs(1)  # 시작점(v)을 1로 설정
=======
>>>>>>> b3aff186a1d5c097ca6eee16c94f06824e0cf529
=======
>>>>>>> 548daa4abe5e97aacab0c6d163197eb688f08bf3
dfs(1) # 시작점(v)을 1로 설정
