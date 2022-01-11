import sys
sys.stdin = open('input.txt')

def dijkstra(s):
    distance[s] = 1

    # 노드의 개수만큼 반복
    for _ in range(N+1):
        min_idx = -1
        min_val = 0
        for i in range(1, N+1):
            if not visited[i] and distance[i] > min_val:
                min_idx = i
                min_val = distance[i]
        visited[min_idx] = 1

        for i in range(1, N+1):
            if mat[min_idx][i] and not visited[i]:  # 연결되어 있고 방문 X
                if distance[min_idx] + mat[min_idx][i] > distance[i]:
                    distance[i] = distance[min_idx] + mat[min_idx][i]

T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]

    # 그래프 표현
    mat = [[0 for _ in range(N+1)] for _ in range(N+1)]
    for s, e in edges:
        mat[s][e] = 1

    # 초기화
    distance = [0 for _ in range(N+1)]
    visited = [0] * (N+1)

    # 다익스트라 시작
    start = 1
    dijkstra(start)
    print(distance)
    print('#{} {}'.format(tc, distance[N]))