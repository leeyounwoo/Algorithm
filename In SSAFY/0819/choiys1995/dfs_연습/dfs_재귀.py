<<<<<<< HEAD
import sys
sys.stdin = open('input.txt')

def dfs(v):
    visited[v] = 1
    print(v, end=' ') # 현재 방문 노드 출력

    # 현재 노드(v)와 인접한 노드 찾기
    for w in range(1, V+1):
        # 만약 방문한 적 없고, 연결되어 있다면
        if G[v][w] == 1 and visited[w] == 0:
            # 인접한 노드(w)를 가지고서 다음 dfs 실행
            # 즉, 이웃 노드(w)가 새로운 v가 됨
=======
def dfs(v):
    visited[v] = 1
    print(v, end = " ")

    for w in range(1, V+1):
        if G[v][w] == 1 and visited[w] == 0:
>>>>>>> 594c4091f9746ad09dd55cc5689632c610d27bfd
            dfs(w)

V, E = map(int, input().split())
temp = list(map(int, input().split()))

<<<<<<< HEAD
G = [[0 for _ in range(V+1)] for _ in range(V+1)] # 인접 행렬
visited = [0 for _ in range(V+1)]

for i in range(0, len(temp)-1, 2):
    G[temp[i]][temp[i+1]] = 1 # 인접한 노드 표기
    G[temp[i+1]][temp[i]] = 1 # 반대 방향도 표기

for i in range(V+1):
    for j in range(V+1):
        print(G[i][j], end=' ')
    print()
=======
G = [[0 for _ in range(V+1)] for _ in range(V+1)]
visited = [0 for _ in range(V+1)]

for i in range(0, len(temp)-1, 2):
    G[temp[i]][temp[i+1]] = 1 # 인접 노드
    G[temp[i+1]][temp[i]] = 1 # 반대 방향 (무방향 이므로)

for i in range(V+1):
    for j in range(V+1):
        print(G[i][j], end = " ")
    print()

dfs(1)
>>>>>>> 594c4091f9746ad09dd55cc5689632c610d27bfd
