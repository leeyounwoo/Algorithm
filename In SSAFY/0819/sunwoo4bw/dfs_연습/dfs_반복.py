import sys
sys.stdin = open('input.txt')


def dfs(v):  # 시작점(v)을 1로 설정
    stack = []
    stack.append(v)  # 시작 지점 스택에 삽입

    while stack:  # 내가 갈 곳이 있으면 계속 돌 수 있을때까지 돌아 = stack이 안 비어 있을 때까지
        # 순회 시작!
        v = stack.pop()  # 현재 방문하려는 노드

        if visited[v] == 0:  # 내가 방문하려는 노드에 한 번도 방문하지 않았으면
            visited[v] = 1  # 방문표기
            print(v, end=" ")  # 현재 방문한 노드 출력

            for w in range(1, V + 1):  # 내가 다음에 갈, 인접 노드 순회
                if G[v][w] == 1 and visited[w] == 0:  # 인접 노드 중 갈 수 있는 곳이라면
                    # 스택에 내가 다음으로 갈 곳을 넣어
                    stack.append(w)


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
    G[temp[i + 1]][temp[i]] = 1  # 반대 방향도 표기(무방향 그래프이므로) -방향성이 있는 그래프라면 이 반대 표기 안해줘도 되겠지!


# for i in range(V+1):
#     for j in range(V+1):
#         print(G[i][j], end=' ')
#     print()

dfs(1)  # 시작점(v)을 1로 설정
