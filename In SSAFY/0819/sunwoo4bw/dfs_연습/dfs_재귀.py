import sys
sys.stdin = open('input.txt')


def dfs(v):
    visited[v] = 1
    print(v, end=' ') # 현재 방문 노드 출력

    # 현재 노드(v)와 인접한 노드 찾기
    for w in range(1, V+1):
        # 만약 방문한 적 없고, 연결되어 있다면...
        if G[v][w] == 1 and visited[w] == 0:
            # 인접한 노드(w)를 가지고서 다음 dfs 실행
            # 즉, 이웃 노드(w)가 새로운 v가 됨
            dfs(w)
            # 재귀가 코드가 더 간결하지만! 1000번 이상이면 stack overflow발생!


# 노드가 V, 간선이 E
V, E = map(int, input().split())
temp = list(map(int, input().split()))  # 1 2 1 3 ...
# 그래프
G = [[0 for _ in range(V + 1)] for _ in range(V + 1)]  # node개수보다 하나 더 많게 인접행렬
visited = [0 for _ in range(V + 1)]  # 0으로 초기화

for i in range(0, len(temp) - 1, 2):  # 간선의 개수만큼 반복문 돌아 아니면 temp의 길이만큼 돌아도 돼
    # 두 개씩 잘라서 생각해줄겨
    # temp[i]
    # temp[i+1]
    G[temp[i]][temp[i + 1]] = 1  # 인접한 노드 표기
    G[temp[i + 1]][temp[i]] = 1  # 반대 방향도 표기(무방향 그래프이므로)

# for i in range(V+1):
#     for j in range(V+1):
#         print(G[i][j], end=' ')
#     print()

dfs(1)  # 시작점(v)을 1로 설정


# 재귀랑 반복의 출력값이 다른 이유
# 반복문에서는 인접노드순회를 stack에 넣어주지
# 재귀는 인접한 노드를 찾으면 바로 함수 실행 -