import sys
sys.stdin = open('input.txt')

# prim
def find_MST(s):
    # 시작 지점은 0으로
    key[s] = 0

    # 정점의 개수만큼 반복
    for _ in range(V):
        # 방문하지 않은 정점 중, 최소 가중치를 가진 정점 찾기 매순간 최소값 찾기
        min_idx = -1
        min_val = float('inf')
        for i in range(V+1):
            if not visited[i] and key[i] < min_val:
                min_idx = i
                min_val = key[i]
        # 현재 최소 가중치를 가진 정점(== min_idx)
        # 방문 처리
        visited[min_idx] = 1

        # 인접 노드들을 확인하면서
        for i in range(V + 1):
            # 이웃 노드와 연결되어있고 방문한 적이 없다면
            if mat[min_idx][i] and not visited[i]:
                # 인접 정점들의 key 값을 필요하다면 갱신
                weight = mat[min_idx][i]
                if weight < key[i]:
                    key[i] = weight # 더 작은 키 값으로 갱신
                    parents[i] = min_idx # 이웃 노드의 부모 노드 변경

T = int(input())
for tc in range(1, T +1):
    V, E = map(int, input().split())

    # 인접행렬
    mat = [[0 for _ in range(V + 1)] for _ in range(V + 1)] # V + 1 * V + 1
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        mat[n1][n2] = w
        mat[n2][n1] = w

    # 초기화
    key = [float('inf')] * (V + 1)  # 초기 각 노드의 가중치는 무한대로 초기화
    parents = [None] * (V + 1)  # 부모 정점 리스트 초기화
    visited = [0] * (V + 1)  # 방문 배열 초기화

    start = 0 # 시작점
    find_MST(start)

    # parents가 이루는 트리가 결국 MST가 됨
    print('#{} {}'.format(tc, sum(key)))