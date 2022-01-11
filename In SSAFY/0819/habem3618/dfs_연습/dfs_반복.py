import sys
sys.stdin = open('input.txt')

def dfs(v):
    stack = []
    stack.append(v)  # 시작 지점 스택에 삽입

    while stack:  # 순회 시작
        v = stack.pop()  # 현재 방문 노드

        if visited[v] == 0:
            visited[v] = 1   # 방문 표기
            print(v, end=" ")  # 현재 방문한 노드 출력

            for w in range(1, V+1):  # 인접 노드 순회
                if G[v][w] == 1 and visited[w] == 0:  # 인접 노드 중 갈 수 있는 곳이라면
                    stack.append(w)

V, E = map(int, input().split())  # 7 8
temp = list(map(int, input().split()))  # 1 2 1 3 ...

G = [[0 for _ in range(V+1)] for _ in range(V+1)]
visited = [0 for _ in range(V+1)]

for i in range(0, len(temp)-1, 2):
    G[temp[i]][temp[i+1]] = 1  # 인접한 노드 표기
    G[temp[i+1]][temp[i]] = 1  # 반대 방향도 표기(무방향 그래프이므로)

# 인접 행렬 출력 테스트
# # for i in range(V+1):
# #     for j in range(V+1):
# #         print(G[i][j], end=" ")
# #     print()

dfs(1) # 시작점(v)을 1로 설정