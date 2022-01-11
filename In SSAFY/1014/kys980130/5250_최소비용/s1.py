import sys
sys.stdin = open('input.txt')
def dijkstra(s):
    distance[s] = 0

    # 노드의 개수만큼 반복
    for _ in range(N+1):

        # 현재 위치에서 가장 가까운 거리에 있는 노드 찾기
        min_i = -1
        min_j = -1
        min_val = float('inf')
        for i in range(N+1):
            for j in range(N+1):
                if not visited[i][j] and distance[i][j] < min_val:
                    min_i = i
                    min_j = j
                    min_val = distance[i][j]
        visited[i][j] = 1

        # 해당 노드로부터 인접한 노드들의 거리 살펴보기
        for i in range(N+1):
            for j in range(N+1):
                if not visited[i]:  # 연결되어 있고 방문한 적 없는지 체크
                    # 현재 위치까지 오는데 걸린 거리 + 현재 위치로
                    if distance[min_i][min_j] < distance[i][j]:
                        distance[i] = distance[min_idx] + mat[min_idx][i]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    distance = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * (N + 1) for _ in range(N+1)]

    # 다익스트라 시작
    start = 0
    dijkstra(start)

    # N까지 도달하는데 드는 최소 비용 == distance[N]
    print(f'#{tc} {distance[N]}')