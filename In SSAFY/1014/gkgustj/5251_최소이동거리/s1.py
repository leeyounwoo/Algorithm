import sys
sys.stdin = open('input.txt')

def dijkstra(start):
    distance[start] = 0

    # 노드의 개수만큼 반복
    for _ in range(N+1):
        min_idx = -1
        min_value = float('inf')

        for i in range(N+1):
            if not visited[i] and distance[i] < min_value:
                min_idx = i
                min_value = distance[i]
        
        visited[min_idx] = 1

        for i in range(N+1):
            if mat[min_idx][i] and not visited[i]:
                distance[i] = min(distance[i], distance[min_idx]+mat[min_idx][i])


T = int(input())

for t in range(1, T+1):
    N, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]

    # 인접 행렬
    mat = [[0 for _ in range(N+1)] for _ in range(N+1)]
    for s, e, w in edges:
        mat[s][e] = w
    
    visited = [0 for _ in range(N+1)]
    distance = [float('inf') for _ in range(N+1)]

    dijkstra(0)

    print('#{} {}'.format(t, distance[N]))