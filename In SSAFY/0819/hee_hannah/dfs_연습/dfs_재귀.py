import sys
sys.stdin = open('input.txt')

def dfs(v):
    visited[v] = 1
    print(v, end=" ") # 현재 방문 노드 출력

    # 현재 노드 (v)와 인접한 노드 찾기
    for w in range(1, V+1):
        # 만약 방문한 적 없고 연결되어있다면
        if G[v][w] == 1 and visited[w] == 0:
            # 인접한 노드 (w)를 가지고서 다음 dfs실행
            # 즉 이웃 노드w가 새로운 v가됨 (1000번 넘어가지않도록 주의 오버플로우)
            dfs(w)



V, E = map(int, input().split()) # 노드와 간선
temp = list(map(int, input().split()))

G = [[0 for _ in range(V+1)] for _ in range(V+1)] # 인접행렬

visited = [0 for _ in range(V+1)]

for i in range(0, len(temp)-1, 2): # 두개씩 잘라
    G[temp[i]][temp[i+1]] = 1 # 인접한 노드 표기
    G[temp[i+1]][temp[i]] = 1 # 반대 방향도 표기(무방향 그래프이므로)
for i in range(V+1): # 인접행렬출력테스트
    for j in range(V+1):
        print(G[i][j], end=" ")
    print()

dfs(1) # 시작점v를 1로 설정

# 재귀랑 인접(반복)이랑 결과가 다름..
# 반복은 스택에 넣음 2 3
# 반면 재귀는 찾으면 바로 실행함 바로 2실행
