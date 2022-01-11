import sys
sys.stdin = open('input.txt')


def find_MST(s):
    key[s] = 0

    # 정점의 개수만큼 반복
    for _ in range(V):
        # 방문하지 않은 정점 중, 최소 가중치를 가진 정점 찾기
        min_idx = -1
        min_val = float('inf')
        for i in range(V+1):
            if not visited[i] and key[i] < min_val:
                min_idx = i
                min_val = key[i]

        # 현재 최소 가중치를 가진 정점 (== min_idx)
        # 방문 처리
        visited[min_idx] = 1

        # 인접 노드들을 확인하면서
        for i in range(V+1):
            # 이웃 노드와 연결되어있고 방문한 적이 없다면
            if adj_mat[min_idx][i] and not visited[i]:
                # 인접 정점들의 key 값을 필요하면 갱신
                weight = adj_mat[min_idx][i]
                if weight < key[i]:
                    key[i] = weight       # 더 작은 키 값으로 갱신
                    parents[i] = min_idx  # 이웃 노드의 부모 노드 변경


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]

    # 인접 행렬
    adj_mat = [[0 for _ in range(V+1)] for _ in range(V+1)]
    for n1, n2, w in edges:
        adj_mat[n1][n2] = w
        adj_mat[n2][n1] = w

    # 초기화
    key = [float('inf')] * (V + 1)  # 초기 각 노드의 가중치는 무한대로 초기화
    parents = [None] * (V + 1)      # 부모 정점 리스트 초기화
    visited = [0] * (V + 1)         # 방문 배열 초기화

    s = 0
    find_MST(s)


# parents가 이루는 트리가 결국 MST가 됨
    print("#{} {}".format(tc, sum(key)))

