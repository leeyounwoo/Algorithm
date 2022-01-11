import sys
sys.stdin = open('input.txt')

def dijkstra(s):
    distance[s] = 0

    # 노드의 개수만큼 반복
    for _ in range(n+1):

        # 현재 위치에서 가장 가까운 거리에 있는 노드 찾기
        min_idx = -1
        min_val = float('inf')
        for i in range(n+1):
            if not visited[i] and distance[i] < min_val:
                min_idx = i
                min_val = distance[i]
        visited[min_idx] = 1

        # 해당 노드로부터 인접한 노드들의 거리 살펴보기
        for i in range(n+1):
            if mat[min_idx][i] and not visited[i]: # 연결되어 있고 방문한적 없는지 체크
                if distance[min_idx] + mat[min_idx][i] < distance[i]:
                    distance[i] = distance[min_idx] + mat[min_idx][i]

t = int(input())
for tc in range(1, t+1):
    n, e = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(e)]

    # 그래프 표현 (인접행렬)
    mat = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for s, e, w in edges:
        mat[s][e] = w

    # 초기화
    distance = [float('inf') for _ in range(n+1)]
    visited = [0] * (n+1)

    # 다익스트라 시작
    start = 0
    dijkstra(start)

    print(f'#{tc} {distance[n]}')