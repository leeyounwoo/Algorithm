import sys
sys.stdin = open('input.txt')


def find_MST(s):
    key[s] = 0 # 시작점만 먼저 0으로

    # 정점의 개수만큼 반복
    for _ in range(v+1): # 0번 노드포함이니까
        # 방문하지 않은 정점 중, 최소 가중치를 가진 정점 찾기 매순간 최소값 찾기
        min_idx = -1
        min_val = float('inf')
        for i in range(v+1): # key = [0, 무한, 무한,,,,]
            if not visited[i] and key[i] < min_val: # 0 < 무한
                min_idx = i # 0 찾아질것
                min_val = key[i] # 0
        # 현재 최소 가중치를 가진 정점(== min_idx)
        # 방문 처리
        visited[min_idx] = 1

        # 인접 노드들을 확인하면서
        for i in range(v + 1):
            # 이웃 노드와 연결되어있고(값이 존재하고) 방문한 적이 없다면
            if mat[min_idx][i] and not visited[i]:
                # 인접 정점들의 key 값을 필요하다면 갱신
                weight = mat[min_idx][i] # weight 변수에 w 가중치 담아
                if weight < key[i]: # ex. 가중치 < 무한
                    key[i] = weight # 더 작은 키 값으로 갱신
                    parents[i] = min_idx # 이웃 노드의 부모 노드 변경


t = int(input())
for tc in range(1, t+1):
    v, e = map(int, input().split())
    mat = [[0 for _ in range(v + 1)] for _ in range(v + 1)] # 값을 넣을 빈 배열
    for _ in range(e):
        start, end, w = map(int, input().split())
        mat[start][end] = mat[end][start] = w # 무방향

    # 초기화
    key = [float('inf')] * (v + 1)  # 초기 각 노드의 가중치는 무한대로 초기화
    parents = [None] * (v + 1)  # 부모 정점 리스트 초기화
    visited = [0] * (v + 1)  # 방문 배열 초기화

    start = 0
    find_MST(start)


    print('#{} {}'.format(tc, sum(key))) # 최소 가중치의 합
