import sys
sys.stdin = open('input.txt')

def dfs(v):
    visited[v] = 1
    print(v, end=" ")  # 현재 방문 노드 출력

    # 현재 노드(v)와 인접한 노드 찾기
    for w in range(1, V+1):
        # 만약 방문한적 없고, 연결되어 있다면...
        if G[v][w] == 1 and visited[w] == 0:
            # 인접한 노드(w)를 가지고서 다음 dfs 실행
            # 즉, 이웃 노드(w)가 새로운 v가 됨
            dfs(w)

V, E = map(int,input().split())  # 7, 8
temp = list(map(int, input().split()))  # 1 2 1 3 2 4 ...

G = [[0 for _ in range(V+1)] for _ in range(V+1)]
visited = [0 for _ in range(V+1)]

for i in range(0, len(temp)-1, 2):
    G[temp[i]][temp[i+1]] = 1  # 인접한 노드 표기
    G[temp[i+1]][temp[i]] = 1  # 무방향 그래프이므로 반대 방향도 표기

dfs(1)
